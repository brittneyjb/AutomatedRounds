import spotipy
import random
import time
from spotipy.oauth2 import SpotifyOAuth

# important variables

user_id = # TODO: Spotify user id to go here
laptop = # TODO: Spotify laptop device id to go here
# can make other device id variables

bb_wcs = 'spotify:playlist:2EmFhQbtOCRkb8yfFhZIoN', #Brittney giant wcs playlist
bb_blues = 'spotify:playlist:7cINyALIfKcc6UV4b5aG54', #Brittney blues wcs playlist


#setup spotipy
scope = "user-read-playback-state,user-modify-playback-state,playlist-modify-public,user-library-modify,playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

#spotipy functions

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
    
# TODO: important function for both randomization and to improve general in order playlist function
def num_songs_in_playlist(playlist):
    return -1;


# rounds functions

#TODO: Implement better
def fadeout():
    for x in range(90, 0, -5):
        volume(x)

#TODO: make randomization of songs work and edit this
# This will return both the next song uri to be played, and the index to be added to songs_played
def next_random_song(playlist, songs_played):
    return -1;


def playlist_in_order(playlist, in_order, song_len, wait_len):
    volume(100)
    sp.start_playback(device_id=laptop, context_uri=playlist)
    for i in range(50): #arbitrary number for now
        print("HERE")
        time.sleep(song_len) # 25) TESTING
        fadeout()
        pause()
        time.sleep(wait_len) # 10) TESTING
        if i < 49:
            volume(100)
            next()
            play()
    return 1

#TODO: make randomization of songs work and edit this
def playlist_random_order(playlist, song_len, wait_len):
    volume(0)
    sp.start_playback(device_id=laptop, context_uri=playlist)

    for i in range(50): #arbitrary number for now
        print("HERE")
        time.sleep(song_len) # 25) TESTING
        fadeout()
        pause()
        time.sleep(wait_len) # 10) TESTING
        if i < 49:
            volume(100)
            next()
            play()
    return 1



print("Welcome to Spotipy WCS Practice")
pl_choice = input("What playlist do you want? Options: blues, general\n")
in_order = create = False if input("Play the playlist in order? (y/n)  ")[0] in 'nN' else True
song_length = int(input("How long do you want the song to go for? (in seconds, eg 60 for 1 minute)\n"))
wait_length = int(input('How long should I wait to play the next song? (also in seconds)\n'))

playlist = ''
if pl_choice.contains('b'):
    playlist =  bb_blues
else:
    playlist = bb_wcs

if in_order:
    playlist_in_order(playlist, song_length, wait_length)
else:
    print('playing songs randomly from a playlist isn\'t implemented yet, sorry')

