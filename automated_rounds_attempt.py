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
        time.sleep(90) #TESTING
        for x in range(90, 0, -5):
            volume(x)
        pause()
        time.sleep(17) #TESTING
        if i < dances - 1:
            volume(100)
            next()
            play()
    return 1


#Spotipy Setup
scope = "user-read-playback-state,user-modify-playback-state,playlist-modify-public,user-library-modify,playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Important Id's
user_id = "ut8uqu3o1rdhyuuu76sk545gf"
laptop = '07d1cf60406513896e7d1e5ee96e445b83ccb76a'
phone = '3cc0c159ac3af78dee2e28619a5f200a64d1ba01'

rounds_playlists = [
    ('Brittney Made a Rounds Playlist', 'spotify:playlist:74cMK3dTapj9LOLLVdpt14'),
    ('Just Another Rounds Playlist', 'spotify:playlist:6SjoefPMI3jqCIHHICisjg'),
    ('Mostly Stolen from Erin 1hr', 'spotify:playlist:1LzWNrpynPGRyK6vGeNr8V'),
    ('Erin Round 4', 'spotify:playlist:00E2lhBAuoh9KeClY4sJSV'),
    ('Erin Round 6', 'spotify:playlist:4oiQuwhGMXjrYZzmuK2Ma5'),
    ('Erin Round 7', 'spotify:playlist:5Z8VovGPWMmUwg4l7oYB8w')
]

style_playlists = {
    'standard': [
        ('waltz', 'spotify:playlist:3tySq93kdHZO5q9uc0ehH0'),
        ('tango', 'spotify:playlist:0GVhyJpq4fSLeHGc1qzTPT'),
        ('vwaltz', 'spotify:playlist:2x6xsJaLaSRIHtvFBLydFc'),
        ('foxtrot', 'spotify:playlist:5mCQN8F6KdwqCvyDKzgR2k'),
        ('quickstep', 'spotify:playlist:1J2agKYZsWS9ixlz835yxn')
    ],
    'smooth': [
        ('waltz', 'spotify:playlist:5XcRq5MExfvU8CX44Ijzpl'),
        ('tango', 'spotify:playlist:6YNKfwBXcz2zHNX1TiyG9c'),
        ('foxtrot', 'spotify:playlist:4PirFi4xCnNt0XxP23cIuZ'),
        ('vwaltz', 'spotify:playlist:1Zc7QslS7B9t11PmCzFfYn')
    ],
    'latin': [
        ('samba', 'spotify:playlist:5nQulnltzrziO093GNHg9x'),
        ('cha', 'spotify:playlist:6cTchFw9vS6BlXTxWNou1x'),
        ('rumba', 'spotify:playlist:5G159Z30efAsIIwYeIjwjC'),
        ('jive', 'spotify:playlist:3C8sdKT1bZf8g3l8UXCvik')
    ],
    'rhythm': [
        ('cha', 'spotify:playlist:5IW9TKPkrzzaAkIWpY2VJw'),
        ('rumba', 'spotify:playlist:4UPnU85FNSQJhCBFU4X5pz'),
        ('swing', 'spotify:playlist:6IYTGFTZMSOWCuNRb9oECM'),
        ('bolero', 'spotify:playlist:5Punjypn7pBwntjHXcDZFT'),
        ('mambo', 'spotify:playlist:5TTw3HZThOMny3hO9AJGTr')
    ]
}

def get_song(dance):
    playlist = ''
    try:
        playlist = sp.playlist_items(dance)
    except:
        print('error getting dance tracks')
    #print(playlist)
    index = random.randint(0, len(playlist['items'])-1)
    song = playlist['items'][index]['track']['uri']
    print('got song: ' + song)
    return song

def add_songs(playlist_id, songs):
    #try:
    sp.user_playlist_add_tracks(user_id, playlist_id, songs)
    #except:
        #print('error adding tracks')
    #print('add_song ' + song + ' to ' + playlist_id)
    return 

def make_playlist(round_type, style):
    playlist_name = style + " " + round_type + " spotipy"
    playlist = ''
    try:
        playlist = sp.user_playlist_create(user_id, playlist_name)
    except:
        print('create playlist error')
    #print(playlist)
    tracks = []
    if round_type == 'continuous':
        for i in range(3):
            for dance,id in style_playlists[style]:
                tracks.append(get_song(id))
        add_songs(playlist['uri'], tracks)
    else:
        for dance,id in style_playlists[style]:
            tracks.append(get_song(id))
        add_songs(playlist['uri'], tracks)
    return playlist['uri']


def delete_playlist(uri):
    try:
        sp.current_user_unfollow_playlist(uri)
    except:
        print('Error deleting playlist')
    return

round_type = "continuous" # options: normal, continuous

if round_type == "normal":
    current_playlist = rounds_playlists[random.randint(0, len(rounds_playlists)-1)]
    print(current_playlist[0])

    # Standard (5-dance)
    dance_round(5, current_playlist[1])
    # Smooth (4-dance)
    input("Ready to continue to smooth?")
    dance_round(4)
    # Latin (4-dance)
    input("Ready to continue to latin?")  
    dance_round(4)
    # Rhythm (5-dance)
    input("Ready to continue to rhythm?")
    dance_round(5)

if round_type == "continuous":
    print('not done')
    style = input('What style?').lower()
    legal_styles = ['standard', 'smooth', 'latin', 'rhythm']
    while style not in legal_styles:
        style = input('actually choose a legal style: ')
    playlist = make_playlist(round_type, style)
    num_dances = 4
    if style.lower() in ['standard', 'rhythm']:
        num_dances = 5
    for i in range(3):
        dance_round(num_dances)
        input('ready to continue? ')
    print('Completed ' + style + ' continuous round.')
    delete_playlist(playlist)


    
    #print(jives)
    #jive_song = jives['items'][random.randint(0, jives['total']-1)]['track']['id']
    
