# Standup Skill

Generate a daily standup by combining Linear issues, Calendar, and local meeting notes.

## Usage

```
/standup
```

Or: "Generate my standup" / "What's my standup for today?"

## What It Does

1. **Pulls Linear issues** - Gets issues assigned to you (filter by project if specified)
2. **Gets today's calendar** - Lists meetings from PY Demo Calendar
3. **Reads recent meeting notes** - Checks `meetings/` folder for blockers and context
4. **Formats standup** - Creates a ready-to-share update

## Instructions for Claude

When the user runs `/standup`:

1. **Get Linear issues assigned to me:**
   - Use `mcp__linear-server__list_issues` with `assignee: "me"`
   - Filter to in-progress or high priority items

2. **Get today's calendar:**
   - Use `mcp__google-workspace__get_events` for today's date
   - Calendar: `9c0fed61bfb892cd256b45ecf4e89ca56878e612e13c9575de107f070b4367b2@group.calendar.google.com`
   - Email: `carlvellotti@gmail.com`

3. **Read recent meeting notes:**
   - Glob for `meetings/*.md`
   - Read the most recent 2-3 notes
   - Look for lines containing "blocker", "waiting on", "blocked by"

4. **Format and output:**

```
## Standup - [Date]

### Working On
- [CAR-XX]: [Title] (Priority)
- [CAR-XX]: [Title] (Priority)

### Today's Meetings
| Time | Meeting |
|------|---------|
| HH:MM | Meeting name |

### Blockers
- [Blocker from notes or "None"]
```

## Requirements

- Linear MCP connected
- Google Workspace MCP connected
- Recent meeting notes in `meetings/`

## Optional Flags

- `/standup moltbot` - Filter Linear issues to Moltbot project only
- `/standup --post` - Also post to Slack after generating
