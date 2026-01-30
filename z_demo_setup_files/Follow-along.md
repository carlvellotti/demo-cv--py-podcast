# Claude Code for PMs: The Complete Guide

**Watch Carl Vellotti demo how to turn Claude Code into your PM command center.**

[VIDEO EMBED PLACEHOLDER]

---

## Get the Files

Everything in this demo uses the **PM Copilot OS** — a folder structure designed for PMs working with Claude Code.

**[Download from GitHub](https://github.com/carlvellotti/demo-cv--py-podcast)**

```bash
git clone https://github.com/carlvellotti/demo-cv--py-podcast.git
cd demo-cv--py-podcast
```

---

## Section 1: Connect Claude Code to Google Workspace

**What you'll do:** Give Claude access to your Gmail, Calendar, Drive, Docs, and Sheets.

### Step 1: Google Cloud Console

1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Create a new project (name it anything)
3. Go to **APIs & Services → Library**
4. Enable these APIs:
   - Google Calendar API
   - Google Drive API
   - Gmail API
   - Google Docs API
   - Google Sheets API
5. Go to **APIs & Services → OAuth consent screen**
   - Choose "External"
   - Add your email as a test user
6. Go to **APIs & Services → Credentials**
   - Create OAuth 2.0 Client ID
   - Choose "Desktop app"
   - Copy the **Client ID** and **Client Secret**

### Step 2: Install the MCP Server

```bash
pip install workspace-mcp
```

### Step 3: Configure Claude Code

Add to your `.mcp.json`:

```json
{
  "mcpServers": {
    "google-workspace": {
      "command": "~/.local/bin/workspace-mcp",
      "env": {
        "GOOGLE_OAUTH_CLIENT_ID": "your_client_id_here",
        "GOOGLE_OAUTH_CLIENT_SECRET": "your_client_secret_here"
      }
    }
  }
}
```

### Step 4: Verify

Restart Claude Code, then run:

```
/mcp
```

You should see `google-workspace` listed. The first time you use a Google command, you'll be prompted to authorize via browser.

---

## Section 2: Real PM Workflow — Meeting Prep

**What happens:** Claude pulls your calendar, finds related docs in Drive, reads your local meeting notes, and suggests updates to your Google Docs.

### The Prompt

> Help me prep for today's meetings. Look at my calendar events for today, find relevant meeting docs in google drive, check my local notes, compare against agendas, and suggest additions to each doc for approval.

### What Claude Does

1. Pulls your calendar events
2. Searches Google Drive for meeting docs
3. Reads local meeting notes from `meetings/`
4. Compares notes against agendas
5. Suggests additions to each doc
6. Writes directly to Google Docs (with your approval)

**Key insight:** Claude pulled from 3 sources (Calendar, Drive, local files) and wrote back to Docs — all in one workflow.

---

## Section 3: Writing Back

Claude isn't read-only. It can:

- Create calendar events
- Move and organize files in Drive
- Send emails via Gmail
- Update Google Docs and Sheets

For anything else, there's [Chrome MCP](https://github.com/anthropics/anthropic-quickstarts/tree/main/mcp-server-chrome) as a catch-all.

---

## Section 4: Other Integrations

### 4A. Linear (Issue Tracking)

**Setup — one command:**

```bash
claude mcp add --transport http linear-server https://mcp.linear.app/mcp
```

**Try it:**

> What are my Linear tickets for the Moltbot project?

**Then:**

> Update the project to the new name of OpenClaw instead of MoltBot (official rename) – update it across the entire project and tickets.

---

### 4B. Slack

Slack MCP uses "stealth mode" — browser tokens that don't require admin approval.

**Try it:**

> Send an update about the name change and overall status of the project to #all-the-full-stack-pm channel in slack

---

### 4C. Reddit (User Research)

> What are the top discussions in r/productmanagement this week? Give me the titles of the posts and current upvotes.

Quick user research without leaving Claude.

---

### 4D. Standup Generator

**The power move:** Combine multiple integrations into one workflow.

> Generate my standup for today, combines Linear issues + Calendar + meeting notes. Output: Working on, Today's meetings, Blockers.

Claude pulls from Linear, Calendar, and your local meeting notes to generate a complete standup.

---

## Section 5: The PM OS Reveal

**The secret:** Everything in this demo runs from a single folder structure — the PM Copilot OS.

### Folder Structure

```
pm-copilot-os/
├── CLAUDE.md           # The brain — Claude reads this first
├── context/            # Background info (team, product, goals)
├── meetings/           # Meeting notes by date
├── projects/           # Each project gets its own folder + CLAUDE.md
├── templates/          # Reusable templates and personas
├── todos/              # Task tracking (tasks.md, backlog.md)
├── tools/              # Scripts and utilities Claude can run
├── workflows/          # Multi-step processes
├── .claude/skills/     # Custom slash commands
└── _temp/              # Scratch space
```

### Key Files

- **CLAUDE.md** — Like onboarding a new team member. Claude reads this to understand how to help you.
- **projects/[name]/CLAUDE.md** — Project-specific context. `cd` into a project folder and Claude has full context.
- **workflows/** — Reusable multi-step processes with their own instructions.

---

## Section 6: PM Skills Demo

Skills are reusable slash commands that encode your expertise.

### 6A. frontend-design (A/B Comparison)

> Bash open both /Users/carl/Documents/Carl's Life OS/📦 Projects/peter-yang-podcast-prep/demo-folder/_temp so I can see them.

Same prompt, dramatically different results based on whether the skill is active.

- **WITH skill:** Retro-terminal brutalism design
- **WITHOUT skill:** Generic purple SaaS page

Skills encode design taste and expertise — not just instructions.

---

### 6B. stakeholder-review

Run any document through multiple reviewer personas.

> /stakeholder-review projects/moltbot-v2/prd.md

**What happens:**
- Exec reviewer: Strategic concerns, ROI questions
- Engineer reviewer: Technical feasibility, edge cases
- Designer reviewer: UX issues, accessibility

Personas live in `templates/personas/` — part of your OS.

---

### 6C. consult-the-council

Query multiple frontier models for diverse perspectives.

> /consult-the-council Should we build the mobile app first or focus on improving the web experience? --effort low

**The Council:**
- GPT-5.2 Thinking (OpenAI)
- Gemini 3 Pro (Google)
- Grok 4 (xAI)

Use `--effort low|medium|high` to control depth vs. speed.

---

### 6D. generate-image

Generate and iterate on images with session memory.

> Generate a user journey of someone using a proactive, always-on AI assistant that reminds them about stuff throughout the day

**Then refine:**

> Now make it in Studio Ghibli style

The skill maintains session context so you can iterate without re-describing.

---

## Section 7: Build a Skill from Scratch

**The progression:** Workflows → Skills

### Step 1: Start with a Workflow

Look at `workflows/standup-generator/CLAUDE.md` — it describes the multi-step process.

### Step 2: Formalize as a Skill

Create `.claude/skills/standup/SKILL.md`:

```markdown
# /standup

Generate a daily standup combining Linear, Calendar, and meeting notes.

## Instructions

1. Get today's calendar events
2. Get my assigned Linear issues (in progress or recently updated)
3. Read recent meeting notes from meetings/
4. Output in this format:

**Working on:**
- [Linear issues]

**Today's meetings:**
- [Calendar events]

**Blockers:**
- [Any blockers mentioned in notes or issues]
```

### Step 3: Use It

> /standup

**Key insight:** Document your workflows, then formalize them into skills. Your expertise compounds over time.

---

## Section 8: Get Started

### Clone the Repo

```bash
git clone https://github.com/carlvellotti/demo-cv--py-podcast.git
cd demo-cv--py-podcast
```

### Add Your Keys

1. Copy `.env.example` to `.env`
2. Add your API keys:
   - `GEMINI_API_KEY` — for image generation
   - `OPENAI_API_KEY` — for consult-the-council
   - `GROK_API_KEY` — for consult-the-council

### Configure MCPs

Follow the setup docs in the repo:
- `SETUP-GOOGLE-MCP.md`
- `SETUP-LINEAR-MCP.md`
- `SETUP-REDDIT-MCP.md`

### Start Using

```bash
cd demo-cv--py-podcast
claude
```

Try:
> What's on my calendar today?

---

## Key Takeaways

1. **Claude as operational hub** — Not just chat, but takes action across your tools
2. **MCP is the standard** — One protocol, many integrations
3. **Context is everything** — CLAUDE.md + folder structure = Claude understands your work
4. **Skills encode expertise** — Reusable patterns that compound over time
5. **Start simple, grow over time** — You don't need all of this day one

---

## Questions?

Join the conversation: [The Full Stack PM](https://fullstackpm.com)
