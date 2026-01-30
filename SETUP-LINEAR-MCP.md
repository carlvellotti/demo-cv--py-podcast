# Linear MCP Setup Guide

**Contrast to Google:** This is the "easy" end of the spectrum - one command setup.

---

## Setup (One Command!)

```bash
claude mcp add --transport http linear-server https://mcp.linear.app/mcp
```

That's it. Run `/mcp` in Claude Code to authenticate.

---

## What It Can Do

| Action | Example |
|--------|---------|
| List issues | "Show my urgent issues" |
| Create issue | "Create an issue: Add dark mode - low priority" |
| Update issue | "Move CAR-60 to In Progress" |
| Add comments | "Add comment to CAR-61: Blocked on security review" |
| List projects | "What projects do I have?" |
| Create projects | "Create a project called X" |
| List cycles/sprints | "What's in the current sprint?" |
| Search | "Find issues about deployment" |

---

## Demo Project Created

**Project:** Moltbot Integration (topical - 60k+ stars on GitHub)

**Issues created for demo:**

| ID | Title | Priority |
|----|-------|----------|
| CAR-60 | Evaluate Moltbot deployment options | Urgent |
| CAR-61 | Set up Slack channel integration | High |
| CAR-62 | Create custom Moltbot skills for PM workflows | High |
| CAR-63 | Security review: API key management and data access | Urgent |
| CAR-64 | Team rollout: Training and adoption plan | Medium |

Each issue has realistic PM content:
- Overview sections
- Acceptance criteria
- Checklists
- Technical considerations

---

## Demo Script

**Setup demo (show contrast to Google):**

"Now let me show you the other end of the spectrum. Some MCPs are incredibly easy. Linear - one command:"

```bash
claude mcp add --transport http linear-server https://mcp.linear.app/mcp
```

"Restart, run /mcp to authenticate, done."

**Usage demo:**

"What are my urgent issues?"
→ Shows CAR-60, CAR-63

"Create an issue: Research WhatsApp integration for Moltbot - medium priority, add to Moltbot Integration project"
→ Creates issue instantly

"Add a comment to CAR-60: Completed cost analysis, recommending Docker approach"
→ Adds comment

---

## Cleanup (Before Live Demo)

Delete the demo issues if you want a clean slate:
- Either delete via Linear UI
- Or use MCP: "Delete issues CAR-60 through CAR-64"

Or keep them - they're realistic enough to demo with.

---

## Notes from Testing

- Setup: Literally one command + restart + /mcp auth
- Auth flow: Opens browser, click "Authorize", done
- Response time: Fast, <1 second for most operations
- Issue creation: Supports full markdown in descriptions
- Project creation: Works, can set icon/color/priority
