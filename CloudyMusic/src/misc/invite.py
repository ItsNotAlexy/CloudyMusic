import nextcord
import wavelink
from nextcord.ext import commands

class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def invite(self, ctx):
        e = nextcord.Embed(
            title="Invite Me!",
            description="[Click Me!](https://discord.com/api/oauth2/authorize?client_id=1058000020806303774&permissions=8&scope=bot%20applications.commands)"
        )
        await ctx.send(embed=e)


def setup(bot):
    bot.add_cog(Invite(bot))