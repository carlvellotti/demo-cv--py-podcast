# Reddit MCP Setup Guide

**Use case:** Community research, trend monitoring, competitive intel

---

## Setup

```bash
pip install mcp-server-reddit
```

Then add to `.mcp.json`:

```json
{
  "mcpServers": {
    "reddit": {
      "type": "stdio",
      "command": "/Users/YOUR_USERNAME/.local/bin/mcp-server-reddit",
      "args": []
    }
  }
}
```

**Note:** No API key needed - uses public Reddit API.

---

## What It Can Do

| Action | Example |
|--------|---------|
| Get frontpage | "What's trending on Reddit?" |
| Subreddit info | "Tell me about r/productmanagement" |
| Hot posts | "What's hot on r/startups?" |
| New posts | "Show new posts in r/SaaS" |
| Top posts | "Top posts from r/productmanagement this week" |
| Rising posts | "What's rising in r/technology?" |
| Post content | "Read the full post [id]" |
| Comments | "Get comments on [post]" |

### Time filters for top posts
- `hour`, `day`, `week`, `month`, `year`, `all`

---

## PM Use Cases

**1. Community Research**
"What are the top complaints in r/productmanagement this month?"

**2. Competitive Intel**
"What are people saying about [competitor] in r/SaaS?"

**3. Trend Monitoring**
"What's trending in r/artificial this week?"

**4. User Research**
"Find posts about [pain point] in r/startups"

**5. Content Ideas**
"What questions are people asking in r/ProductManagement?"

---

## Demo Script

"Reddit is gold for understanding what real users and PMs are thinking. Let me show you..."

"What are the top posts in r/productmanagement this week?"

→ Shows list including (ironically) complaints about PM-fluencers with complicated Claude setups

"Let me read the top one..."

→ Gets full post content

"What are people saying in the comments?"

→ Gets discussion

"This is real-time community research without leaving your terminal."

---

## Notes from Testing

- No auth required - works out of the box
- Fast responses
- Can get full post content + comments
- Time filters work well (week, month, etc.)
- Good for: research, trends, sentiment
- Path issue: Make sure to use `/Users/carl/.local/bin/mcp-server-reddit` not uvx
