from disnake.ext import commands
import random

class Prediction(commands.Cog):

    def __init___(self,bot):
        self.bot = bot
   

    @commands.slash_command(name="prediction", description="Получить ответы на все ваши вопросы, если вы затрудняетесь в ответе.")
    async def ping(ctx, message):
        variant = random.randint(0, 4)
        if variant == 0:
            await ctx.send("Да")
        elif variant == 1:
            await ctx.send("Нет")
        elif variant == 2:
            await ctx.send("Наверное")
        elif variant == 3:
            await ctx.send("Скорее да, чем нет")
        else:
            await ctx.send("Скорее нет, чем да")

def setup(bot):
    bot.add_cog(Prediction(bot)) 