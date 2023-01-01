import nextcord
import json
import os
from nextcord.ext import commands

bot = commands.Bot(command_prefix="s:", help_command=None, intents=nextcord.Intents.all())

for src in os.listdir("./src/music"):
    if src.endswith(".py"):
        bot.load_extension(f"src.music.{src[:-3]}")

for src in os.listdir("./src/misc"):
    if src.endswith(".py"):
        bot.load_extension(f"src.misc.{src[:-3]}")

for src in os.listdir("./src/events"):
    if src.endswith(".py"):
        bot.load_extension(f"src.events.{src[:-3]}")

with open("./config/config.json") as f:
    config = json.load(f)

bot.run(config['BOT_CONFIG']['TOKEN'])