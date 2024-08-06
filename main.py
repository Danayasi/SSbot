import config
import random
import disnake
from disnake.ext import commands


intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print("Готов!")


@bot.slash_command(name="beat", description="Избей своего друга или врага?")
async def ping(ctx, tobeat:disnake.Member):
    await ctx.send(f"{ctx.author.mention} избивает {tobeat.mention}")

@bot.slash_command(name="random", description="Получить случайное число в промежутке введёных чисел.")
async def ping(ctx, first_number:int, second_number:int):
    await ctx.send(f"Выбрано число в промежутке от {first_number} до {second_number}. Это число - {random.randint(first_number, second_number)}")


@bot.slash_command(name="clear", description="Очистить X количество сообщений.")
async def clear(self, interaction, amount: int):
    await interaction.response.send_message(f"Удалено {amount} сообщений.")
    await interaction.channel.purge(limit=amount + 1)


@bot.slash_command(name="avatar", description="Взять аватар человека.")
async def avatar(self, interaction, member: disnake.Member = None):
    user = member or interaction.author
    embed = disnake.Embed(title="Аватарка", color=0xff5252)
    embed.set_image(url=user.avatar.url)
    await interaction.response.send_message(embed=embed)


bot.run(config.token)