from disnake.ext import commands
import random

class Prediction(commands.Cog):

    def __init___(self,bot):
        self.bot = bot
   

    @commands.command( )
    async def on_message(self,message):
        if self.bot.user.mention in message.content:
            variant = random.randint(0, 4)
            if variant == 0:
                message.channel.send("Да")
            elif variant == 1:
                message.channel.send("Нет")
            elif variant == 2:
                message.channel.send("Наверное")
            elif variant == 3:
                message.channel.send("Скорее да, чем нет")
            else:
                message.channel.send("Скорее нет, чем да")

def setup(bot):
    bot.add_cog(Prediction(bot)) 