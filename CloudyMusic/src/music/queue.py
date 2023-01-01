import nextcord
import wavelink
import json
from nextcord.ext import commands

with open("config/emojies.json") as f:
    data = json.load(f)
    status_code_ok = data['OK']
    status_code_err = data['ERROR']

class Queue(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['q'])
    async def queue(self, ctx:commands.Context):
        if not ctx.voice_client:
            await ctx.send(f'{status_code_err} | You currently not playing anything.')
        elif not ctx.author.voice:
            return await ctx.send(f'{status_code_err} | Please join a voice channel before running this command.')
        elif ctx.author.voice.channel != ctx.me.voice.channel:
            return await ctx.send(f'{status_code_err} | I must be inside of the same voice channel as you!')
        else:
            vc: wavelink.Player = ctx.voice_client

        if vc.queue.is_empty:
            return await ctx.send(f'{status_code_err} There is no songs in the queue!')
        
        else:
            q_list = vc.queue.copy()
            count = 0

            e = nextcord.Embed(title=f"{ctx.guild.name}'s Queue")
            for song in q_list:
                count += 1

                e.add_field(name=count, value=f"`{song.title}`", inline=False)

            return await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Queue(bot))