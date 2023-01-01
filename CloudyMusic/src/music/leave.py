import nextcord
import wavelink
import json
from nextcord.ext import commands

with open("config/emojies.json") as f:
    data = json.load(f)
    status_code_ok = data['OK']
    status_code_err = data['ERROR']

class Disconnect(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def disconnect(self, ctx:commands.Context):
        if not ctx.voice_client:
            await ctx.send(f'{status_code_err} | You currently not playing anything.')
        elif not ctx.author.voice:
            return await ctx.send(f'{status_code_err} | Please join a voice channel before running this command.')
        elif ctx.author.voice.channel != ctx.me.voice.channel:
            return await ctx.send(f'{status_code_err} | I must be inside of the same voice channel as you!')
        else:
            vc: wavelink.Player = ctx.voice_client

        await vc.disconnect()
        leave_message = nextcord.Embed(
            title="Left the voice channel!",
            description="Thank you for using Cloudy Music! We hope you have very wonderful time while using our bot! We really love your support that you have givin to us by inviting our bot!",
            color=nextcord.Color.random()
        )
        await ctx.send(embed=leave_message)

def setup(bot):
    bot.add_cog(Disconnect(bot))