import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

brittney = "ut8uqu3o1rdhyuuu76sk545gf"
erin = 'clowningninja'
gtbdc = '4a7dnk5bfxtpu7shp2p0jbzjn'
jwolf = 'thebestpony'
chase = '2237qkmxz7bujr6kj5ikz5wli'
laptop = '07d1cf60406513896e7d1e5ee96e445b83ccb76a'
phone = '3cc0c159ac3af78dee2e28619a5f200a64d1ba01'
bolero = 'spotify:playlist:5Punjypn7pBwntjHXcDZFT'

#This finds the Playlist IDs
#pl = sp.user_playlists(user=brittney)
#print(pl)
#for x in pl['items']:
#    print(x['name'] + "\t" + x['uri']) 

#pl = sp.user_playlists(user=erin)
#for x in pl['items']:
#    print(x['owner']['display_name'] + '\t' + x['name'] + "\t" + x['uri'])

#offset = 0

#while True:
#    response = sp.playlist_items('spotify:playlist:3C8sdKT1bZf8g3l8UXCvik',
"""                                  offset=offset,
                                 fields='items.track.id,total',
                                 additional_types=['track'])

    if len(response['items']) == 0:
        break

    print(response['items'])
    offset = offset + len(response['items'])
    print(offset, "/", response['total'])
 """

print(sp.playlist_items(bolero))