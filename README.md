# discord-py-components

[![GitHub release](https://img.shields.io/github/v/release/rb1412bo/discord-py-components)](https://github.com/rb1412bo/discord-py-components/releases)  
[![License: MIT](https://img.shields.io/github/license/rb1412bo/discord-py-components)](LICENSE)

A flexible `discord.py` extension that provides full support for all Discord Components V2 types:

- ActionRow, Button, Select menus (String, User, Role, Mentionable, Channel)  
- DatePicker, TextDisplay  
- Separator (Type 14), Container (Type 17)  
- Automatic setting of the `IS_COMPONENTS_V2` flag  
- No manual HTTP requests in your bot code  

---

## Installation

Ensure you have Python ≥ 3.8 and `discord.py` ≥ 2.0 installed. Then, in your project folder:

```bash
pip install -U git+https://github.com/rb1412bo/discord-py-components.git#egg=discord-py-components
```
 
---
# Quickstart

```py
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

# Load the extension
bot.load_extension("discord_components")

@bot.command()
async def demo(ctx):
    sep = bot.ComponentsV2["Separator"](spacing=2)
    cont = bot.ComponentsV2["Container"](
        components=[{"type": 10, "content": "Inside Container"}],
        accent_color=0xFF00FF
    )
    await ctx.send(
        content="Components V2 Demo",
        components_v2=[sep, cont]
    )

bot.run("YOUR_TOKEN")

```
