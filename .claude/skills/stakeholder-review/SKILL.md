# Stakeholder Review Skill

Run a document through multiple stakeholder personas to get diverse feedback before the real review.

## Usage

```
/stakeholder-review [document]
```

Or: "Review this PRD from different stakeholder perspectives"

## What It Does

1. Reads the document you specify
2. Loads reviewer personas from `templates/personas/`
3. Reviews the document from each perspective
4. Consolidates feedback into actionable items

## Personas Available

- **Executive** (`exec-reviewer.md`) - VP-level, cares about business impact, ROI, timeline
- **Engineer** (`engineer-reviewer.md`) - Technical feasibility, architecture, edge cases
- **Designer** (`designer-reviewer.md`) - User experience, accessibility, user research

## Output Format

```
## Stakeholder Review: [Document Name]

### Executive Perspective
**Overall:** [Approve / Concerns / Block]
- [Key feedback point]
- [Question they would ask]

### Engineering Perspective
**Overall:** [Approve / Concerns / Block]
- [Technical feedback]
- [Question they would ask]

### Design Perspective
**Overall:** [Approve / Concerns / Block]
- [UX feedback]
- [Question they would ask]

### Consolidated Action Items
1. [Must address before review]
2. [Should address]
3. [Consider for future]
```

## Example

```
User: /stakeholder-review projects/moltbot-v2/prd.md

Claude: Running stakeholder review with 3 personas...

## Stakeholder Review: Moltbot v2 PRD

### Executive Perspective
**Overall:** Concerns
- Success metrics are good, but what's the revenue impact?
- "What happens to our growth if a competitor ships this first?"

### Engineering Perspective
**Overall:** Approve with questions
- ML batch processing every 5 min is reasonable
- "What's the fallback if model confidence is below threshold?"

### Design Perspective
**Overall:** Concerns
- No mention of empty states or first-time user experience
- "Have we validated that users understand what 'learning period' means?"

### Consolidated Action Items
1. Add revenue impact estimate to Goals section
2. Define ML confidence threshold and fallback behavior
3. Add first-time user experience to Design section
```

## Tips

- Run this before sending docs for real stakeholder review
- Use the feedback to strengthen weak areas
- Add custom personas for your specific stakeholders
