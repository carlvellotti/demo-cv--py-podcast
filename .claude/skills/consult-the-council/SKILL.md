# /consult-the-council Command

Query multiple frontier AI models for diverse perspectives on a question or problem.

## The Council

| Model | Provider | Low | Medium | High |
|-------|----------|-----|--------|------|
| **GPT-5.2 Thinking** | OpenAI | `reasoning_effort: low` | `reasoning_effort: medium` | `reasoning_effort: xhigh` |
| **Gemini 3 Pro** | Google | `thinking_level: LOW` | `thinking_level: LOW`* | `thinking_level: HIGH` |
| **Grok 4** | xAI | Built-in | Built-in | Built-in |

*Gemini 3 Pro only supports LOW or HIGH (no medium option).
*Grok 4 has built-in reasoning that cannot be adjusted.

## Effort Levels

| Level | Speed | Depth | Best For |
|-------|-------|-------|----------|
| `--effort low` | Fast | Quick takes | Simple questions, brainstorming |
| `--effort medium` | Balanced | Moderate | General questions, validation |
| `--effort high` | Slow | Thorough | Complex problems, critical decisions |

Default is `high` for deepest analysis.

## When to Use

- Stuck on a hard problem and want multiple perspectives
- Validating an approach before committing
- Exploring different ways to solve something
- Getting a second (and third, and fourth) opinion
- Complex architectural or strategic decisions

## Usage

The user will provide a question or context. Run the council script and present the responses.

## Instructions

1. **Run the script** with the user's question and optional effort level:
   ```bash
   cd "/Users/carl/Documents/Carl's Life OS/📦 Projects/peter-yang-podcast-prep/demo-folder/tools/image_gen" && python3 ".scripts/consult_council.py" "USER'S QUESTION HERE" --effort high
   ```

2. **Choose effort level** based on the question:
   - `--effort low` - Quick responses for brainstorming or simple questions
   - `--effort medium` - Balanced for general questions
   - `--effort high` - Thorough analysis for complex decisions (default)

3. **Wait for responses** - high effort can take several minutes

4. **Present the council's responses** in a clear format, highlighting:
   - Areas of agreement across models
   - Unique insights from each model
   - Any contradictions or different approaches
   - Your synthesis/recommendation based on the council's input

5. **If a model fails**, note it but continue with the others

## Examples

**Quick brainstorm (low effort):**
```bash
cd "/Users/carl/Documents/Carl's Life OS/📦 Projects/peter-yang-podcast-prep/demo-folder/tools/image_gen" && python3 ".scripts/consult_council.py" "What are some creative names for a PM productivity app?" --effort low
```

**Standard question (medium effort):**
```bash
cd "/Users/carl/Documents/Carl's Life OS/📦 Projects/peter-yang-podcast-prep/demo-folder/tools/image_gen" && python3 ".scripts/consult_council.py" "Should I use SQLite or PostgreSQL for my new SaaS app?" --effort medium
```

**Complex decision (high effort, default):**
```bash
cd "/Users/carl/Documents/Carl's Life OS/📦 Projects/peter-yang-podcast-prep/demo-folder/tools/image_gen" && python3 ".scripts/consult_council.py" "Should I use SQLite or PostgreSQL for my new SaaS app? Consider scalability, operational complexity, and modern deployment patterns." --effort high
```

Then present the three perspectives with your synthesis.

## Configuration

The script uses these environment variables from `.env`:
- `OPENAI_API_KEY`
- `GEMINI_API_KEY`
- `GROK_API_KEY`

Models and parameters can be adjusted in `.scripts/consult_council.py`.
