# PM Copilot OS

This is your AI-powered PM workspace. Claude reads this file automatically to understand how to help you.

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
| `_temp/` | Scratch space - anything here can be deleted |

## Key Files

- `tasks.md` - Current active work
- `backlog.md` - Ideas and future work

## How to Use

**Starting a project:** Create a folder in `projects/`, add a CLAUDE.md with project context, then `cd` into it.

**Running a workflow:** Go to `workflows/<name>/` and follow the CLAUDE.md there.

**Adding context:** Drop files in `_temp/` for one-off tasks, or add to `context/` if it's recurring.

## Connected Tools

This workspace connects to:
- **Google Workspace** - Calendar, Drive, Docs (via MCP)
- **Linear** - Issue tracking (via MCP)
- **Slack** - Team communication (via MCP)

## My Preferences

- Keep responses concise
- Use bullet points over paragraphs
- Ask clarifying questions before big changes
- Reference specific files when making suggestions
