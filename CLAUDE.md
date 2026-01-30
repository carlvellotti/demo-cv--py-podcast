# PM Copilot OS

This is your AI-powered PM workspace. Claude reads this file automatically to understand how to help you.

## Live Demo Context

This workspace is being used for a live demo on the Peter Yang podcast. See the full run of show: `../RUN-OF-SHOW.md`

When Carl says "Section X" or references a demo section, follow along with that document.

## What This Is

A structured folder system for product managers to work with Claude Code. Everything has a place, and Claude knows where to find it.

## Folder Structure

| Folder | Purpose |
|--------|---------|
| `context/` | Background info Claude should always know (team, product, goals) |
| `meetings/` | Meeting notes - flat folder, named by date |
| `projects/` | Each project gets its own folder with its own CLAUDE.md |
| `templates/` | Reusable templates for docs, personas, etc. |
| `tools/` | Scripts and utilities Claude can run |
| `workflows/` | Multi-step workflows with their own instructions |
| `todos/` | Task tracking - tasks.md and backlog.md |
| `_temp/` | Scratch space - anything here can be deleted |

## Key Files

- `todos/tasks.md` - Current active work
- `todos/backlog.md` - Ideas and future work

## How to Use

**Starting a project:** Create a folder in `projects/`, add a CLAUDE.md with project context, then `cd` into it.

**Running a workflow:** Go to `workflows/<name>/` and follow the CLAUDE.md there.

**Adding context:** Drop files in `_temp/` for one-off tasks, or add to `context/` if it's recurring.

## Connected Tools

This workspace connects to:
- **Google Workspace** - Calendar, Drive, Docs (via MCP)
- **Linear** - Issue tracking (via MCP)
- **Slack** - Team communication (via MCP)

## Skills (Slash Commands)

| Command | What It Does |
|---------|--------------|
| `/standup` | Generate daily standup from Linear + Calendar + meeting notes |
| `/generate-image [prompt]` | Generate images via Gemini, saves to `tools/image_gen/outputs/` |
| `/stakeholder-review [doc]` | Run a document through exec/eng/design personas for feedback |
| `/consult-the-council [question]` | Query GPT-5.2, Gemini 3, and Grok 4 for diverse perspectives |

## My Preferences

- Keep responses concise
- Use bullet points over paragraphs
- Ask clarifying questions before big changes
- Reference specific files when making suggestions
