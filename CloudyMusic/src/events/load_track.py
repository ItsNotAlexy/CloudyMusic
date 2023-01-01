import nextcord
import json
import wavelink
from nextcord.ext import commands

class TrackEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_wavelink_track_end(self, player:wavelink.Player, track:wavelink.Track, reason):
        ctx = player.ctx
        vc = ctx.voice_client

        if vc.stop:
            if vc.loop:
                return await vc.play(track)
            else:
                return

        if vc.loop:
            return await vc.play(track)

        if vc.queue:
            next_song = vc.queue.get()
            await vc.play(next_song)
            await ctx.send(f'Now playing: {next_song.title}')
        else:
            await vc.play(track)
    
def setup(bot):
    bot.add_cog(TrackEvents(bot))