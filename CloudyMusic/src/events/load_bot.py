import nextcord
import json
import wavelink
from nextcord.ext import commands

class Botevent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("----------------------------")
        print("[INFO] Bot Logged In!")
        print(f"[INFO] Bot User: {self.bot.user}")
        print(f"[INFO] Bot ID: {self.bot.user.id}")
        print("----------------------------")
    
def setup(bot):
    bot.add_cog(Botevent(bot))