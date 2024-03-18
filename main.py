import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import config

#spotifyインスタンスを作成
sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=config.CLIENT_ID,
	    client_secret=config.CLIENT_SECRET
    )
)

results = sp.search(q="LE SSERAFIM", limit=1, type="track")
print(type(results))
#pprint.pprint(results)
# print(di['items']['name'])
for track in results["tracks"]["items"]:
#    track_name = track['release_date']
    print(track["album"]["images"])
