import spotipy
import time
from pygame import mixer
from spotipy.oauth2 import SpotifyOAuth

# important variables

user_id = # TODO: Spotify user id to go here
laptop = # TODO: Spotify laptop device id to go here 
# can make other device id variables

bb_wcs = 'spotify:playlist:2EmFhQbtOCRkb8yfFhZIoN' #Brittney giant wcs playlist
bb_blues = 'spotify:playlist:7cINyALIfKcc6UV4b5aG54' #Brittney blues wcs playlist
lucy_2_25 = 'spotify:playlist:4vHguqo8koIpFj6wflpqM5'


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

#TODO: Implement better
def fadeout():
    for x in range(90, 0, -5):
        volume(x)

def command_sound(cmd, wait_time):
    mixer.init()
    if cmd == 'discuss':
        mixer.music.load('./spoken/discussl.mp3')
    if cmd == 'switch':
        mixer.music.load('./spoken/rotate.mp3')
    mixer.music.play()
    time.sleep(wait_time)



def practice_playlist(pl, shuffle, song_len, wait_len):
    volume(100)
    sp.shuffle(shuffle, laptop)
    command_sound('discuss', wait_len)
    sp.start_playback(device_id=laptop, context_uri=pl) 
    play()
    for i in range(10): #arbitrary number for now
        print("HERE")
        time.sleep(song_len) # 25) TESTING
        fadeout()
        pause()
        command_sound('discuss', wait_len)
        if i < 9:
            command_sound('switch', wait_len)
            command_sound('discuss', wait_len)
            volume(100)
            next()
            play()
    return 1



print("Welcome to Spotipy WCS Practice")

# This setup is just an example
pl_choice = input("What playlist do you want? Options: blues, general\n")
shuffle = True #create = False if input("Shuffle playlist? (y/n)  ")[0] in 'nN' else True
song_length = 90 #int(input("How long do you want the song to go for? (in seconds, eg 60 for 1 minute)\n"))
wait_length = 45 #int(input('How long should I wait to play the next song? (also in seconds)\n'))

pl = bb_wcs
if pl_choice == 'blues':
    pl =  bb_blues

# Required calls
mixer.init()
practice_playlist(pl, shuffle, song_length, wait_length)
