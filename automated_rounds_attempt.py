import os
import sys
import time
import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def next():
    try:
        sp.next_track()
    except:
        print("next error")

def play():
    try:
        sp.start_playback()
    except:
        print('start playback error')

def pause():
    try:
        sp.pause_playback()
    except:
        print('pause error')

def volume(vol):
    try:
        sp.volume(vol)
    except:
        print('volume error')



def dance_round(dances, playlist=None):
    volume(100)
    if playlist:
        sp.start_playback(device_id=laptop, context_uri=playlist)
    else:
        next()
        play()
    for i in range(dances):
        print("HERE")
        time.sleep(20)  #90) TESTING
        for x in range(90, 0, -5):
            volume(x)
        pause()
        time.sleep(10) #20)  TESTING
        if i < dances - 1:
            volume(100)
            next()
            play()
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
erin_round_4 = 'spotify:playlist:00E2lhBAuoh9KeClY4sJSV'
erin_round_6 = 'spotify:playlist:4oiQuwhGMXjrYZzmuK2Ma5'
erin_round_7 = 'spotify:playlist:5Z8VovGPWMmUwg4l7oYB8w'

playlists = [
    brittney_made_a_rounds_playlist_id,
    just_another_rounds_playlist_id,
    mostly_stolen_from_erin_1hr_id,
    erin_round_4,
    erin_round_6,
    erin_round_7
]

current_playlist = playlists[random.randint(0, len(playlists)-1)]
print(current_playlist)

#Standard
dance_round(5, current_playlist)

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