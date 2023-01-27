import os
import sys
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def dance_round(dances, playlist=None):
    sp.volume(100)
    if playlist:
        sp.start_playback(device_id=laptop, context_uri=playlist)
    else:
        sp.next_track()
        try:
            sp.start_playback()
        except:
            print("error")
    for i in range(dances):
        print("HERE")
        time.sleep(20)  #90) TESTING
        for x in range(90, 0, -5):
            sp.volume(x)
        sp.pause_playback()
        time.sleep(10) # TESTING  45)
        if i < dances - 1:
            sp.next_track()
            sp.volume(100)
            try:
                sp.start_playback()
            except:
                print("error")
    return 1


#Spotipy Setup
scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Important Id's
user_id = "ut8uqu3o1rdhyuuu76sk545gf"
laptop = '07d1cf60406513896e7d1e5ee96e445b83ccb76a'
phone = '3cc0c159ac3af78dee2e28619a5f200a64d1ba01'

#Playlists:
brittney_made_a_rounds_playlist_id = 'spotify:playlist:74cMK3dTapj9LOLLVdpt14'
just_another_rounds_playlist_id = 'spotify:playlist:6SjoefPMI3jqCIHHICisjg'
mostly_stolen_from_erin_1hr_id = 'spotify:playlist:1LzWNrpynPGRyK6vGeNr8V'


#Standard
dance_round(5, brittney_made_a_rounds_playlist_id)

#Breathe Break
input("Ready to continue to smooth?")

# Smooth: (4 dance expected)
dance_round(4)

#Shoe Change Time
input("Ready to continue to latin?")  

# Latin: (4 dance expected)
dance_round(4)

#Breathe break
input("Ready to continue to rhythm?")

#Rhythm Time (5-dance expected)
dance_round(5)