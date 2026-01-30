# Meeting Prep Workflow

This workflow helps you prepare for upcoming meetings by pulling context from multiple sources.

## What It Does

1. **Pulls your calendar** - Gets today's or tomorrow's meetings
2. **Finds related docs** - Searches Google Drive for meeting docs
3. **Reads local notes** - Checks meetings/ folder for relevant context
4. **Compares and suggests** - Identifies gaps between your notes and meeting agendas
5. **Updates docs** - Adds your notes to shared meeting documents (with approval)

## How to Use

Say: "Help me prep for tomorrow's meetings"

Or be specific: "Prep me for the stakeholder review on Friday"

## What You'll Need

- Google Workspace MCP connected (calendar + drive)
- Meeting notes in `meetings/` folder
- Meeting docs in Google Drive

## Example Output

```
Found 3 meetings tomorrow:
1. Sprint Planning (10am) - Doc: Sprint Planning Jan 30
2. 1:1 with Sarah (2pm) - Doc: 1:1 Sarah Running Notes
3. Stakeholder Review (4pm) - Doc: Stakeholder Review Agenda

From your notes, I can add:
- Sprint Planning: Velocity (34 pts), blockers from retro
- Stakeholder Review: Open questions about GDPR, timeline

Want me to add these to the docs?
```

## Tips

- Keep meeting notes in flat files: `meetings/2026-01-28-sprint-retro.md`
- Name Google Docs clearly so Claude can find them
- Run this workflow the day before for best results
