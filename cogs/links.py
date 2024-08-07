from disnake.ext import commands
import random

class Links(commands.Cog):

    def __init___(self,bot):
        self.bot = bot
   

    @commands.slash_command(name="links", description="Наши ссылки.")
    async def ping(ctx):
      await ctx.send("Наш гитхаб: https://github.com/SandStoneHub")

      await ctx.send("Наш сайт: http://sandstone.fun/")

      await ctx.send("Наши игры: https://sandstone-studio.itch.io/")


def setup(bot):
    bot.add_cog(Links(bot)) 