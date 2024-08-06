from disnake.ext import commands
import random

class Randm(commands.Cog):
    def __init___(self,bot):
        self.bot = bot

    @commands.slash_command(name="random", description="Получить случайное число в промежутке введёных чисел.")
    async def ping(ctx, first_number:int, second_number:int):
        await ctx.send(f"Выбрано число в промежутке от {first_number} до {second_number}. Это число - {random.randint(first_number, second_number)}")

def setup(bot):
    bot.add_cog(Randm(bot))