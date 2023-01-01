import nextcord
import wavelink
import json
from nextcord.ext import commands

with open("config/emojies.json") as f:
    data = json.load(f)
    status_code_ok = data['OK']
    status_code_err = data['ERROR']

class Loop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def loop(self, ctx:commands.Context):
        if not ctx.voice_client:
            await ctx.send(f'{status_code_err} | You currently not playing anything.')
        elif not ctx.author.voice:
            return await ctx.send(f'{status_code_err} | Please join a voice channel before running this command.')
        elif ctx.author.voice.channel != ctx.me.voice.channel:
            return await ctx.send(f'{status_code_err} | I must be inside of the same voice channel as you!')
        else:
            vc: wavelink.Player = ctx.voice_client


        try:
            vc.loop ^= True
        except Exception:
            setattr(vc, "loop", False)


        if vc.loop:
            return await ctx.message.add_reaction("🔃")
        else:
            return await ctx.message.add_reaction(status_code_ok)

def setup(bot):
    bot.add_cog(Loop(bot))