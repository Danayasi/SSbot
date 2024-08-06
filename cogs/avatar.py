from disnake.ext import commands
import disnake

class Avatar(commands.Cog):
    def __init___(self,bot):
        self.bot = bot

    @commands.slash_command(name="avatar", description="Получить аватарку человека.")
    async def avatar(self, interaction, member: disnake.Member = None):
        user = member or interaction.author
        embed = disnake.Embed(title=f"Аватарка {member}", color=0xff5252)
        embed.set_image(url=user.avatar.url)
        await interaction.response.send_message(embed=embed)
       

def setup(bot):
    bot.add_cog(Avatar(bot))