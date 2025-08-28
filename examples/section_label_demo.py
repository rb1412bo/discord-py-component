import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
bot.load_extension("discord_components")

@bot.command()
async def section_label(ctx):
    inner_btn = bot.ComponentsV2["Button"](style=3, label="Accept")  # Success style
    lbl = bot.ComponentsV2["Label"](                                # Type 18 label wrapper
        label="Terms",
        description="Accept to continue",
        component=inner_btn
    )
    sec = bot.ComponentsV2["Section"](                              # Type 9 section
        text="Please read the terms below:",
        accessory=lbl
    )
    await ctx.send(components_v2=[sec])

bot.run("YOUR_TOKEN")
