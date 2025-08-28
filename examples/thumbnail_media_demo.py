import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
bot.load_extension("discord_components")

@bot.command()
async def media(ctx):
    thumb = bot.ComponentsV2["Thumbnail"](                         # Type 11 thumbnail
        url="https://placekitten.com/100/100"
    )
    gallery = bot.ComponentsV2["MediaGallery"](                    # Type 12 media gallery
        elements=[
            {"type": 11, "url": "https://placekitten.com/200/200"},
            {"type": 11, "url": "https://placekitten.com/300/200"}
        ]
    )
    await ctx.send(content="Cute cats:", components_v2=[thumb, gallery])

bot.run("YOUR_TOKEN")
