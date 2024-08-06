from disnake.ext import commands
import random

class CoinFlip(commands.Cog):

    def __init___(self,bot):
        self.bot = bot
   

    @commands.slash_command(name="coinflip", description="Подкинуть монетку")
    async def ping(ctx):
        coin = random.randint(0, 1)
        if coin == 0:
            await ctx.send("Орёл.")
        else:
            await ctx.send("Решка.")


def setup(bot):
    bot.add_cog(CoinFlip(bot)) 