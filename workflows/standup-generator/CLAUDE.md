# Standup Generator Workflow

Generates a daily standup by combining data from Linear, Calendar, and local notes.

## What It Does

1. **Pulls Linear issues** - Gets issues assigned to you
2. **Gets today's calendar** - Lists your meetings
3. **Reads recent notes** - Checks for blockers and context
4. **Formats standup** - Creates a ready-to-share update

## How to Use

Say: "Generate my standup for today"

## Output Format

```
## Standup - [Date]

**Working on:**
- [Issue]: [Title] (Priority)
- [Issue]: [Title] (Priority)

**Today's meetings:**
- [Time] - [Meeting name]
- [Time] - [Meeting name]

**Blockers:**
- [Blocker from notes]
```

## What You'll Need

- Linear MCP connected
- Google Calendar MCP connected
- Recent meeting notes in `meetings/`

## Tips

- Works best when your Linear issues are up to date
- Blockers are pulled from meeting notes mentioning "blocker" or "waiting on"
- Can post directly to Slack with: "Generate and post my standup"
