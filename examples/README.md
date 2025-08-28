# Examples for discord-py-components

This folder contains example bots showing how to use the V2 Components –  
including new layout and content components like **Separator**, **Section**, **Container**, **Label**, **Thumbnail**, **MediaGallery** and more.

Each `.py` file is a minimal runnable script you can adapt to your bot.

## Files

- `separator_demo.py` — Show visual spacing between components  
- `section_label_demo.py` — Combine Section and Label for better UX  
- `thumbnail_media_demo.py` — Show images and galleries inside messages  
- `container_combo.py` — Group multiple elements in a styled box

Run any example with:
```bash
python examples/<filename>.py

---

### `examples/separator_demo.py`
```python
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
bot.load_extension("discord_components")

@bot.command()
async def sep(ctx):
    btn1 = bot.ComponentsV2["Button"](style=1, label="Above")   # Primary button
    sep = bot.ComponentsV2["Separator"](spacing=2)              # Adds vertical gap
    btn2 = bot.ComponentsV2["Button"](style=4, label="Below")   # Danger button
    await ctx.send("Buttons with separator:", components_v2=[btn1, sep, btn2])

bot.run("YOUR_TOKEN")

