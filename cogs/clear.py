from disnake.ext import commands


class Clear(commands.Cog):
    def __init___(self,bot):
        self.bot = bot

    @commands.slash_command(name="clear", description="Очистить канал от X кол-ва сообщений.")
    async def clear(self, interaction, amount:int):
       await interaction.response.send_message(f"Удалено {amount} сообщений.")
       await interaction.channel.purge(limit=amount + 1)
       

def setup(bot):
    bot.add_cog(Clear(bot))