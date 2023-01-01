import nextcord
import json
import wavelink
from wavelink.ext import spotify
from nextcord.ext import commands

with open("./src/events/musicdata.json") as f:
    data = json.load(f)

username = data['SPOTIFY_CONFIG']['CLIENT_USER']
clientID = data['SPOTIFY_CONFIG']['CLIENT_ID']
clientSecret = data['SPOTIFY_CONFIG']['CLIENT_SECRET']

class LodeNode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        bot.loop.create_task(self.connect_nodes())
    
    async def connect_nodes(self):
        await self.bot.wait_until_ready()

        await wavelink.NodePool.create_node(bot=self.bot,
                                            host='www.lavalinknodepublic.ml',
                                            port=443,
                                            password='mrextinctcodes',
                                            https=True,
                                            spotify_client=spotify.SpotifyClient(client_id=clientID, client_secret=clientSecret))

    @commands.Cog.listener()
    async def on_wavelink_node_ready(self, node: wavelink.Node):
        print(f'Node: <{node.identifier}> is Loaded.')
    
def setup(bot):
    bot.add_cog(LodeNode(bot))