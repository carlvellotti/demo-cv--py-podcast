# PM Copilot OS - Setup

## Quick Start

1. Clone this repo
2. Copy `.env.example` to `.env`
3. Add your API keys
4. Replace the config values below
5. Start using: `cd pm-copilot-os && claude`

---

## Config Values to Replace

Before using, replace these placeholders throughout the repo:

| Placeholder | Description | Where to Get It |
|-------------|-------------|-----------------|
| `YOUR_EMAIL` | Your Google Workspace email | Your Gmail address |
| `YOUR_CALENDAR_ID` | Calendar to pull events from | Google Calendar settings → Calendar ID |
| `YOUR_LINEAR_PROJECT` | Linear project for demo | Linear → Project → Settings |

### Files to Update

**For Google Calendar integration:**
- When Claude asks for calendar, use your email and calendar ID

**For Linear integration:**
- When referencing projects, use your own project name

---

## Required API Keys (.env)

```bash
# Google Workspace MCP
# Get from: https://console.cloud.google.com/apis/credentials
GOOGLE_CLIENT_ID=your_client_id
GOOGLE_CLIENT_SECRET=your_client_secret

# Linear MCP (uses OAuth - no key needed, just run setup)
# Run: claude mcp add --transport http linear-server https://mcp.linear.app/mcp

# Gemini (for generate-image skill)
# Get from: https://aistudio.google.com/app/apikey
GEMINI_API_KEY=your_gemini_key

# Optional: For consult-the-council
OPENAI_API_KEY=your_openai_key
GROK_API_KEY=your_grok_key
```

---

## MCP Setup

### Google Workspace
See `SETUP-GOOGLE-MCP.md` for full OAuth setup.

### Linear
One command:
```bash
claude mcp add --transport http linear-server https://mcp.linear.app/mcp
```

### Slack (Optional)
See `SETUP-SLACK-MCP.md` for stealth mode setup.

### Reddit (Optional)
```bash
claude mcp add reddit -- npx -y @modelcontextprotocol/server-reddit
```

---

## Verify Setup

Test each integration:

```
"What's on my calendar today?"
"What are my Linear tickets?"
"Generate my standup"
```

If all three work, you're ready.
