import config
import random
import disnake
import os
from disnake.ext import commands
from disnake import Activity, ActivityType


intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print("Готов!")
    await bot.change_presence(status=disnake.Status.idle,activity=Activity(name="за вами",  type=ActivityType.watching))

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")


bot.run(config.token)