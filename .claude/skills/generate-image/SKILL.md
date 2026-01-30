# Generate Image Skill

Generate and iterate on images using Gemini 3 Pro Image.

## Usage

```
/generate-image [prompt]
```

Or: "Generate an image of..." / "Create a visual for..."

## What It Does

1. Takes your prompt and generates an image via Gemini 3 Pro Image
2. Saves output to `tools/image_gen/outputs/` directory
3. Maintains session for multi-turn refinement
4. Supports reference images for style guidance

## The Script

Uses `.scripts/image_gen.py` which provides:

```python
import sys; sys.path.insert(0, '.scripts')
from image_gen import generate, new_session, revert

# Generate new image
generate("a PM dashboard with dark mode", output_name="dashboard")

# Iterate on it (same session)
generate("make the charts more colorful", output_name="dashboard")

# Start fresh
new_session("dashboard")

# Undo last change
revert(1, "dashboard")
```

## Parameters

| Parameter | Default | Options |
|-----------|---------|---------|
| `output_name` | auto | Custom filename (also determines session) |
| `aspect_ratio` | "1:1" | "1:1", "3:4", "4:3", "16:9", "9:16" |
| `resolution` | "1K" | "1K", "2K", "4K" |
| `reference_images` | None | List of image paths for style reference |

## Multi-Turn Refinement

Each `output_name` gets its own session. To iterate:

```python
# Turn 1: Initial generation
generate("minimalist logo for a PM tool called Moltbot", output_name="logo")

# Turn 2: Refine (same session, remembers context)
generate("make it more playful, add a subtle robot element", output_name="logo")

# Turn 3: Color adjustment
generate("try it in purple and teal", output_name="logo")
```

## Instructions for Claude

When the user asks you to generate an image:

1. **Run the generation:**
   ```bash
   cd "/Users/carl/Documents/Carl's Life OS/📦 Projects/peter-yang-podcast-prep/demo-folder/tools/image_gen" && python3 -c "
   import sys; sys.path.insert(0, '.scripts')
   from image_gen import generate
   generate('USER_PROMPT_HERE', output_name='descriptive_name')
   "
   ```

2. **Show the output path** so the user can view it

3. **For refinements**, use the same `output_name` to continue the session

4. **If they want to start over**, call `new_session('name')`

## Example Conversation

```
User: "Generate a hero image for the Moltbot landing page"

Claude: [Runs generate with prompt, output_name="moltbot-hero"]
Generated: tools/image_gen/outputs/moltbot-hero.png

User: "Make it more dynamic, add some motion blur"

Claude: [Runs generate with refinement prompt, same output_name]
Refined: tools/image_gen/outputs/moltbot-hero.png (updated)

User: "Actually go back to the previous version"

Claude: [Runs revert(1, "moltbot-hero")]
Reverted to previous version.
```

## Requirements

- `GEMINI_API_KEY` in `.env`
- `pip install google-genai pillow python-dotenv`
