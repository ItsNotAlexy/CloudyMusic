# CloudyMusic
A very fun and user friendly music bot, Made in python!


# How to use
Setup everything in `CloudyMusic/config/config.json`

```json
{
    "BOT_CONFIG": {
        "TOKEN": "YOUR_BOT_TOKEN",
        "BOT_ID": "YOUR_BOT_ID"
    }
}
```

And the emojies inside of `CloudyMusic/config/emojies.json`


```json
{
    "MUSIC_CD": "EMOJI_HERE",
    "OK": "EMOJI_HERE",
    "ERROR": "EMOJI_HERE"
}
```

And lastly, inside of the `CloudyMusic/src/events/musicdata.json`

```json
{
    "SPOTIFY_CONFIG": {
        "CLIENT_USER": "SPOTIFY_USER",
        "CLIENT_ID": "SPOTIFY_CLIENT_ID",
        "CLIENT_SECRET": "SPOTIFY_CLIENT_SECRET"
    }
}
```

You can use your own lavalink host by modifying the code inside of `CloudyMusic/src/events/load_node.py`

```python
await wavelink.NodePool.create_node(bot=self.bot,
                                    host='www.lavalinknodepublic.ml',
                                    port=443,
                                    password='mrextinctcodes',
                                    https=True,
                                    spotify_client=spotify.SpotifyClient(client_id=clientID, client_secret=clientSecret)
)
```

after your done with that, Install the requirements by running `pip install -r requirements.txt`

After downloading the package you can now run the script with `python run.py` in the `CloudyMusic` directory.
