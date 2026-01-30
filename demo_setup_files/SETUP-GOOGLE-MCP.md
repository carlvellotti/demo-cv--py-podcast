# Google Workspace MCP Setup Guide (From Scratch)

Using [Taylor Wilsdon's google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp)

---

## Part 1: Google Cloud Console Setup

### Step 1.1: Create a Google Cloud Project

1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Click the project dropdown (top left) → "New Project"
3. Name it something like `claude-workspace-mcp`
4. Click "Create"
5. Make sure the new project is selected

**Time estimate:** ~1 min

**Notes from testing:**
- Project name: `mcp-cc-project`
- UI has "Get started" button now, not direct to consent screen

---

### Step 1.2: Enable Required APIs

Enable these APIs (click each link while signed into your project):

1. [Google Calendar API](https://console.cloud.google.com/apis/library/calendar-json.googleapis.com)
2. [Google Drive API](https://console.cloud.google.com/apis/library/drive.googleapis.com)
3. [Gmail API](https://console.cloud.google.com/apis/library/gmail.googleapis.com)
4. [Google Docs API](https://console.cloud.google.com/apis/library/docs.googleapis.com)
5. [Google Sheets API](https://console.cloud.google.com/apis/library/sheets.googleapis.com)
6. [Google Slides API](https://console.cloud.google.com/apis/library/slides.googleapis.com)
7. [Google Forms API](https://console.cloud.google.com/apis/library/forms.googleapis.com)
8. [Google Tasks API](https://console.cloud.google.com/apis/library/tasks.googleapis.com)
9. [Google Chat API](https://console.cloud.google.com/apis/library/chat.googleapis.com)
10. [Custom Search API](https://console.cloud.google.com/apis/library/customsearch.googleapis.com)
11. [Apps Script API](https://console.cloud.google.com/apis/library/script.googleapis.com)

**Tip:** Click "Enable" on each page. It's fast once you get a rhythm.

**Time estimate:** ~3-5 min

**Notes from testing:**
- Can open all 11 in tabs and click Enable quickly
- Use `?authuser=X&project=PROJECT_NAME` in URLs if multiple Google accounts

---

### Step 1.3: Configure OAuth Consent Screen

1. Go to [APIs & Services → OAuth consent screen](https://console.cloud.google.com/apis/credentials/consent)
2. Click "Get started"
3. Enter App name: `Claude Workspace MCP`
4. Enter User support email: your email
5. Select Audience: "External" (unless you have Google Workspace, then "Internal")
6. Enter Developer contact email: your email
7. Click "Create"

---

### Step 1.5: Add Yourself as a Test User

1. Go to [console.cloud.google.com/auth/audience](https://console.cloud.google.com/auth/audience)
2. Under "Test users", click "+ Add users"
3. Enter your email address
4. Click "Save"

**Important:** You must add yourself as a test user or authentication will fail later.

---

### Step 1.5: Create OAuth Credentials

1. Go to [APIs & Services → Credentials](https://console.cloud.google.com/apis/credentials)
2. Click "+ Create Credentials" → "OAuth client ID"
3. Application type: **Desktop app**
4. Name: `Claude Code`
5. Click "Create"
6. Click "Download JSON" to save your credentials file

---

## Part 2: Claude Code Setup

### Step 2.1: Install the MCP server

Open terminal and run:

```bash
# Option A: Using uvx (recommended)
uvx workspace-mcp --help

# Option B: Using pip
pip install workspace-mcp
```

**Notes from testing:**
- `pip install workspace-mcp` installs to `~/.local/bin/workspace-mcp`
- `uvx` may not work in MCP context - use full path instead

---

### Step 2.2: Add to .mcp.json

Create or edit `.mcp.json` in your project root:

```json
{
  "mcpServers": {
    "google-workspace": {
      "type": "stdio",
      "command": "/Users/YOUR_USERNAME/.local/bin/workspace-mcp",
      "args": [],
      "env": {
        "GOOGLE_OAUTH_CLIENT_ID": "YOUR_CLIENT_ID_HERE",
        "GOOGLE_OAUTH_CLIENT_SECRET": "YOUR_CLIENT_SECRET_HERE"
      }
    }
  }
}
```

Replace:
- `YOUR_USERNAME` with your macOS username
- Credentials from downloaded JSON or Step 1.5

**Notes from testing:**
- Use full path, not `uvx` - MCP may not have uvx in PATH
- Find your path: `which workspace-mcp` or check `~/.local/bin/`

---

### Step 2.3: Authenticate

1. Restart Claude Code (or start new session)
2. Run `/mcp` command - should show google-workspace connected
3. Try a command like "What's on my calendar?"
4. First time: MCP returns an OAuth URL - click it
5. Sign in with your Google account, approve all permissions
6. Retry the command - should work now

**Notes from testing:**
- OAuth link is long - Claude can open it via bash
- Must sign in with same account added as test user
- Tokens are cached after first auth

---

### Step 2.4: Test It

Try these commands:
- "List my recent Google Docs"
- "What's on my calendar today?"
- "Search my Drive for [something]"

**Notes from testing:**
-

---

## Total Setup Time

| Step | Estimated | Actual |
|------|-----------|--------|
| 1.1 Create project | 1 min | |
| 1.2 Enable APIs | 3-5 min | |
| 1.3 OAuth consent | 1 min | |
| 1.4 Add test user | 1 min | |
| 1.5 Create credentials | 1 min | |
| 2.1 Install MCP | 1 min | |
| 2.2 Configure | 1 min | |
| 2.3 Authenticate | 1 min | |
| **Total** | **10-12 min** | |

---

## Troubleshooting

### "Access blocked: This app's request is invalid"
- OAuth consent screen not configured
- Or app is in "Testing" mode and your email isn't added as test user

### "API not enabled"
- Go back to Step 1.2 and enable the missing API

### "Invalid client"
- Double-check Client ID and Secret are correct
- Make sure there are no extra spaces

### MCP not loading
- Restart Claude Code after editing .mcp.json
- Check JSON syntax

---

## Demo Script (for live presentation)

"Let me show you how to connect Claude Code to your entire Google Workspace - Drive, Docs, Gmail, Calendar, everything.

First, we need to set up a Google Cloud project. This is a one-time setup that takes about 10 minutes.

[Walk through Google Console steps]

Now that we have our credentials, we add them to our project's MCP config file...

[Show .mcp.json edit]

And now we authenticate...

[Run /mcp, complete OAuth]

Let's test it - 'What's on my calendar today?'

[Show result]

Now Claude can read my docs, search my drive, check my calendar, even draft emails. All through natural language."
