import nextcord
import wavelink
import datetime
import asyncio
import json
from nextcord.ext import commands

with open("config/emojies.json") as f:
    data = json.load(f)
    status_code_ok = data['OK']
    status_code_err = data['ERROR']
    emoji_cd_playing = data['MUSIC_CD']

class Nowplaying(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['np'])
    async def nowplaying(self, ctx:commands.Context):
        if not ctx.voice_client:
            await ctx.send(f'{status_code_err} | You currently not playing anything.')
        elif not ctx.author.voice:
            return await ctx.send(f'{status_code_err} | Please join a voice channel before running this command.')
        elif ctx.author.voice.channel != ctx.me.voice.channel:
            return await ctx.send(f'{status_code_err} | I must be inside of the same voice channel as you!')
        else:
            vc: wavelink.Player = ctx.voice_client

        if not vc.is_playing():
            await ctx.send('You are currently playing nothing...')


        player = wavelink.Player()
        track_duration = vc.track.duration

        position = vc.position
        percentage = 100 * position / track_duration
        
        e = nextcord.Embed(
            title=f"Now Playing - {vc.track.title}",
        )
        e.add_field(
            name="Duration",
            value=f"`{str(datetime.timedelta(seconds=vc.track.duration))}`"
        )
        e.add_field(
            name="Song URL",
            value=f"[Click Me]({str(vc.track.uri)})"
        )
        progress_msg = await ctx.send(embed=e)

        async def update_progress():
            while vc.is_playing():
                position = vc.position
                track_duration = vc.track.duration
                percentage = 100 * position / track_duration
                
                progress_bar = "=" * int(percentage / 5) + "🔘" + "=" * (19 - int(percentage / 5))
                progress_bar = f"{progress_bar}"
                minutes = int(position // 60)
                seconds = int(position % 60)

                new_embed = nextcord.Embed(
                    title=f"{emoji_cd_playing} Now Playing - {vc.track.title} {emoji_cd_playing}",
                    description=f"**[{progress_bar}] `{minutes}:{seconds:02d}`**"
                )
                new_embed.add_field(
                    name="Duration",
                    value=f"`{str(datetime.timedelta(seconds=vc.track.duration))}`"
                )
                new_embed.add_field(
                    name="Song URL",
                    value=f"[Click Me]({str(vc.track.uri)})"
                )                
                await progress_msg.edit(
                    embed = new_embed
                )
                
                await asyncio.sleep(1)

        asyncio.create_task(update_progress())
        
def setup(bot):
    bot.add_cog(Nowplaying(bot))