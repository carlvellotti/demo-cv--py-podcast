#!/usr/bin/env python3
"""
Consult the Council - Query multiple frontier AI models for diverse perspectives.

Usage:
    python3 _Scripts/consult_council.py "Your question here"
    echo "Your question" | python3 _Scripts/consult_council.py

Models (January 2026):
    - OpenAI: gpt-5.2 (reasoning_effort: xhigh) - Thinking variant
    - Google: gemini-3-pro-preview (thinking_level: HIGH)
    - xAI: grok-4-0709 (Grok 4 with built-in reasoning)

Requires:
    pip3 install openai google-genai httpx

Uses API keys from .env: OPENAI_API_KEY, GEMINI_API_KEY, GROK_API_KEY
"""

import argparse
import asyncio
import json
import os
import sys
from pathlib import Path

# Load .env from vault root
VAULT_ROOT = Path(__file__).parent.parent
env_path = VAULT_ROOT / ".env"
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            if line.strip() and not line.startswith("#") and "=" in line:
                key, value = line.strip().split("=", 1)
                os.environ.setdefault(key, value.strip('"').strip("'"))

# Configuration
CONFIG = {
    "openai": {
        "model": "gpt-5.2",  # Thinking variant (Pro is Responses API only)
        "api_key_env": "OPENAI_API_KEY",
        "base_url": "https://api.openai.com/v1",
        "max_tokens": 16384,
        "temperature": 1.0,
        "timeout": 600,  # 10 minutes for xhigh reasoning
    },
    "gemini": {
        "model": "gemini-3-pro-preview",
        "api_key_env": "GEMINI_API_KEY",
        "max_tokens": 16384,
        "temperature": 1.0,
        "timeout": 600,
    },
    "grok": {
        "model": "grok-4-0709",  # Grok 4 base model with built-in reasoning
        "api_key_env": "GROK_API_KEY",
        "base_url": "https://api.x.ai/v1",
        "max_tokens": 16384,
        "temperature": 1.0,
        "timeout": 600,
    },
}

# Effort level mappings per model
# OpenAI GPT-5.2: supports none, minimal, low, medium, high, xhigh
# Gemini 3 Pro: only supports LOW or HIGH (no medium)
# Grok 4: built-in reasoning, no effort parameter (would error if provided)
EFFORT_LEVELS = {
    "low": {
        "openai": {"reasoning_effort": "low"},
        "gemini": {"thinking_level": "LOW"},
        "grok": {},  # No effort control for Grok 4
    },
    "medium": {
        "openai": {"reasoning_effort": "medium"},
        "gemini": {"thinking_level": "LOW"},  # Pro only has LOW/HIGH, use LOW for medium
        "grok": {},
    },
    "high": {
        "openai": {"reasoning_effort": "xhigh"},
        "gemini": {"thinking_level": "HIGH"},
        "grok": {},
    },
}

COUNCIL_NAMES = {
    "openai": "GPT-5.2 Thinking",
    "gemini": "Gemini 3 Pro",
    "grok": "Grok 4",
}


async def query_openai(question: str, effort: str = "high") -> dict:
    """Query OpenAI GPT-5.2 with configurable reasoning effort."""
    try:
        from openai import AsyncOpenAI
    except ImportError:
        return {"provider": "openai", "error": "openai package not installed. Run: pip3 install openai"}

    api_key = os.environ.get(CONFIG["openai"]["api_key_env"])
    if not api_key:
        return {"provider": "openai", "error": f"{CONFIG['openai']['api_key_env']} not found in environment"}

    effort_config = EFFORT_LEVELS[effort]["openai"]

    try:
        client = AsyncOpenAI(
            api_key=api_key,
            base_url=CONFIG["openai"]["base_url"],
            timeout=CONFIG["openai"]["timeout"],
        )

        response = await client.chat.completions.create(
            model=CONFIG["openai"]["model"],
            messages=[{"role": "user", "content": question}],
            max_completion_tokens=CONFIG["openai"]["max_tokens"],
            temperature=CONFIG["openai"]["temperature"],
            **effort_config,
        )

        return {
            "provider": "openai",
            "model": CONFIG["openai"]["model"],
            "effort": effort,
            "response": response.choices[0].message.content,
            "reasoning_tokens": getattr(response.usage, "reasoning_tokens", None),
        }
    except Exception as e:
        return {"provider": "openai", "error": str(e)}


async def query_gemini(question: str, effort: str = "high") -> dict:
    """Query Google Gemini 3 Pro with configurable thinking level."""
    try:
        from google import genai
        from google.genai import types
    except ImportError:
        return {"provider": "gemini", "error": "google-genai package not installed. Run: pip3 install google-genai"}

    api_key = os.environ.get(CONFIG["gemini"]["api_key_env"])
    if not api_key:
        return {"provider": "gemini", "error": f"{CONFIG['gemini']['api_key_env']} not found in environment"}

    effort_config = EFFORT_LEVELS[effort]["gemini"]
    thinking_level = effort_config.get("thinking_level", "HIGH")

    try:
        client = genai.Client(api_key=api_key)

        response = await asyncio.to_thread(
            client.models.generate_content,
            model=CONFIG["gemini"]["model"],
            contents=question,
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(
                    thinking_level=thinking_level,
                ),
                max_output_tokens=CONFIG["gemini"]["max_tokens"],
                temperature=CONFIG["gemini"]["temperature"],
            ),
        )

        return {
            "provider": "gemini",
            "model": CONFIG["gemini"]["model"],
            "effort": effort,
            "response": response.text,
        }
    except Exception as e:
        return {"provider": "gemini", "error": str(e)}


async def query_grok(question: str, effort: str = "high") -> dict:
    """Query xAI Grok 4 with built-in reasoning (no effort control available)."""
    try:
        from openai import AsyncOpenAI
    except ImportError:
        return {"provider": "grok", "error": "openai package not installed. Run: pip3 install openai"}

    api_key = os.environ.get(CONFIG["grok"]["api_key_env"])
    if not api_key:
        return {"provider": "grok", "error": f"{CONFIG['grok']['api_key_env']} not found in environment"}

    # Note: Grok 4 has built-in reasoning with no effort parameter
    # Passing reasoning_effort would cause an error

    try:
        client = AsyncOpenAI(
            api_key=api_key,
            base_url=CONFIG["grok"]["base_url"],
            timeout=CONFIG["grok"]["timeout"],
        )

        response = await client.chat.completions.create(
            model=CONFIG["grok"]["model"],
            messages=[{"role": "user", "content": question}],
            max_tokens=CONFIG["grok"]["max_tokens"],
            temperature=CONFIG["grok"]["temperature"],
        )

        return {
            "provider": "grok",
            "model": CONFIG["grok"]["model"],
            "effort": "built-in",  # Grok 4 always uses built-in reasoning
            "response": response.choices[0].message.content,
        }
    except Exception as e:
        return {"provider": "grok", "error": str(e)}


async def consult_council(question: str, effort: str = "high") -> list[dict]:
    """Query all council members concurrently with specified effort level."""
    tasks = [
        query_openai(question, effort),
        query_gemini(question, effort),
        query_grok(question, effort),
    ]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # Handle any exceptions that weren't caught
    processed = []
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            provider = ["openai", "gemini", "grok"][i]
            processed.append({"provider": provider, "error": str(result)})
        else:
            processed.append(result)

    return processed


def format_output(results: list[dict], question: str, effort: str) -> str:
    """Format council responses as markdown."""
    lines = [
        "# Council Response",
        "",
        f"**Question:** {question}",
        f"**Effort Level:** {effort}",
        "",
        "---",
        "",
    ]

    for result in results:
        provider = result.get("provider", "unknown")
        name = COUNCIL_NAMES.get(provider, provider)
        model = result.get("model", "unknown")
        result_effort = result.get("effort", effort)

        lines.append(f"## {name}")
        lines.append(f"*Model: {model} | Effort: {result_effort}*")
        lines.append("")

        if "error" in result:
            lines.append(f"**Error:** {result['error']}")
        else:
            lines.append(result.get("response", "No response"))

        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Consult the Council of AI Models")
    parser.add_argument("question", nargs="?", help="Question to ask the council")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument(
        "--effort",
        choices=["low", "medium", "high"],
        default="high",
        help="Reasoning effort level: low (fast), medium (balanced), high (thorough, default)"
    )
    args = parser.parse_args()

    # Get question from argument or stdin
    if args.question:
        question = args.question
    elif not sys.stdin.isatty():
        question = sys.stdin.read().strip()
    else:
        print("Error: No question provided", file=sys.stderr)
        print("Usage: python3 consult_council.py 'Your question here'", file=sys.stderr)
        sys.exit(1)

    if not question:
        print("Error: Empty question", file=sys.stderr)
        sys.exit(1)

    effort_desc = {"low": "fast responses", "medium": "balanced", "high": "thorough reasoning"}
    print(f"Consulting the council on: {question[:100]}{'...' if len(question) > 100 else ''}", file=sys.stderr)
    print(f"Effort level: {args.effort} ({effort_desc[args.effort]})", file=sys.stderr)

    results = asyncio.run(consult_council(question, args.effort))

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print(format_output(results, question, args.effort))


if __name__ == "__main__":
    main()
