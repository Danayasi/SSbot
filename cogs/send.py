from disnake.ext import commands
import disnake

class Send(commands.Cog):
    def __init___(self,bot):
        self.bot = bot

    @commands.slash_command(name="send", description="Сгененировать сообщения")
    @commands.has_permissions(administrator=True)
    async def send(self, ctx, text: str, title: str = None, embed: bool = False, img: str = None, channel: disnake.TextChannel = None):
        if embed:

            if title is None:
                await channel.send("Для Embed сообщений **title** обязателен!", ephemeral=True)
                return
            
            embed = disnake.Embed(
                title=title,
                description=text,
                color=0xffa263,
            )

            if img is not None: embed.set_image(url=img)

            await channel.send(embed=embed)
        else:
           await channel.send(f"{text}")
           
def setup(bot):
    bot.add_cog(Send(bot))