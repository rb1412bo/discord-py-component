import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
bot.load_extension("discord_components")

@bot.command()
async def combo(ctx):
    btn = bot.ComponentsV2["Button"](style=1, label="OK")           # Primary button
    select = bot.ComponentsV2["StringSelect"](                      # Dropdown
        custom_id="opt",
        options=[{"label": "One", "value": "1"}, {"label": "Two", "value": "2"}]
    )
    cont = bot.ComponentsV2["Container"](                           # Type 17 container
        components=[btn, select],
        accent_color=0x00FFAA
    )
    await ctx.send(content="Grouped UI elements:", components_v2=[cont])

bot.run("YOUR_TOKEN")
