import random
import disnake
from disnake.ext import commands


intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print("Готов!")


@bot.slash_command(name="jerkoff")
async def ping(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/939879746555232349/1269984047086436403/1666b172eea9558b.gif?ex=66b20c4f&is=66b0bacf&hm=deee799251be8efcd3c804678ef185522c69625e4f541514315facec6c72b1d8&")


@bot.slash_command(name="beat")
async def ping(ctx, who, tobeat):
    await ctx.send(f"{who} избивает {tobeat}")


@bot.slash_command(name="clear")
async def clear(self, interaction, amount: int):
    await interaction.response.send_message(f"Удалено {amount} сообщений.")
    await interaction.channel.purge(limit=amount + 1)


@bot.slash_command(name="avatar")
async def avatar(self, interaction, member: disnake.Member = None):
    user = member or interaction.author
    embed = disnake.Embed(title="Аватарк", color=0xff5252)
    embed.set_image(url=user.avatar.url)
    await interaction.response.send_message(embed=embed)


bot.run("")