import os
import time
import model
from os import system
from player import play_album, play_artist, play_playlist, play_songs, autoplay_thread
from remove import Delete_Playlist, Delete_Song, Delete_Album, Delete_Artist, DeleteFrom_Playlist
from insertion import add_playlist, addto_playlist, add_song, add_album
from view_model import view_playlists, view_albums, view_artists, view_song, view_playlist, view_songs



header = "\
 ____    ____                  _          __            \n\
|_   \  /   _|                (_)        [  |           \n\
  |   \/   |  __   _   .--.   __   .---.  | |   _   __  \n\
  | |\  /| | [  | | | ( (`\] [  | / /'`\] | |  [ \ [  ] \n\
 _| |_\/_| |_ | \_/ |, `'.'.  | | | \__.  | |   \ '/ /  \n\
|_____||_____|'.__.'_/[\__) )[___]'.___.'[___][\_:  /   \n\
                                               \__.'    "


colors = {
    'blue': '\033[94m',
    'pink': '\033[95m',
    'green': '\033[92m',
}


def colorize(string, color):
    if not color in colors:
        return string
    return colors[color] + string + '\033[0m'


def exec_menu(menu):
    while True:
        os.system('cls')
        # Print some badass ascii art header here !
        print(colorize(header, 'pink'))
        print(colorize('version 0.1\n', 'green'))
        for item in menu:
            print(colorize("[" + str(menu.index(item)) + "] ",
                           'blue') + list(item)[0])
        choice = input(">> ")
        try:
            if int(choice) < 0:
                raise ValueError
            # Call the matching function
            if len(menu[int(choice)]) == 3:
                menu[int(choice)][1](menu[int(choice)][2])
            elif len(menu[int(choice)]) == 2:
                menu[int(choice)][1]()
            else:
                break
        except (ValueError, IndexError):
            pass


##############################################
# Playlist interface


def view_pl():
    name = input("Playlist Name: ")
    print('\n1) Name_asc\n2) Name_desc\n3) Album\n4) Genre\n5) Date\n')
    order = input("Order to view: ")
    view_playlist(name, order)
    input("Press [Enter] to continue...")


def add_pl():
    name = input("Playlist Name: ")
    desc = input("Playlist Description: ")
    add_playlist(name, desc)


def addto_pl():
    playlist = input("Playlist Name: ")
    song = input("Song Name: ")
    addto_playlist(playlist, song)


def remove_pl():
    playlist = input("Playlist Name: ")
    Delete_Playlist(playlist)


def removefrom_pl():
    playlist = input("Playlist Name: ")
    song = input("Song Name: ")
    DeleteFrom_Playlist(playlist, song)


def play_pl():
    playlist = input("Playlist Name: ")
    print('\n1) Name_asc\n2) Name_desc\n3) Album\n4) Genre\n5) Date\n6) Shuffle')
    order = input("Order to play: ")
    play_playlist(playlist, order)


##############################################
# Aartist interface

def view_ar():
    view_artists()
    input("\nPress [Enter] to continue...")


def remove_ar():
    artist = input("Artist Name: ")
    Delete_Artist(artist)


def play_ar():
    artist = input("Artist Name: ")
    play_artist(artist)


##############################################
# Album interface

def view_al():
    view_albums()
    input("\nPress [Enter] to continue...")


def add_al():
    album = input("Album Path: ")
    add_album(album)


def remove_al():
    album = input("Album Name: ")
    Delete_Album(album)


def play_al():
    album = input("Album Name: ")
    play_album(album)


##############################################
# Library interface

def view_lib():
    view_songs()
    input("\n\nPress [Enter] to continue...")


def view_so():
    song = input("Song Name: ")
    view_song(song)
    input("\nPress [Enter] to continue...")


def add_so():
    song = input("Song Path: ")
    add_song(song)


def remove_so():
    song = input("Song Name: ")
    Delete_Song(song)


def play_gen():
    genre = input("Genre to play: ")
    play_songs(genre)


##############################################
# Menus

playlist_menu = [
    ["View Playlists", view_playlists],
    ["View Playlist", view_pl],
    ["Add Playlist", add_pl],
    ["Add Song To Playlist", addto_pl],
    ["Remove Playlist", remove_pl],
    ["Remove From Playlist", removefrom_pl],
    ["Play Playlist", play_pl],
    ["Back"]
]

artist_menu = [
    ["View Artists", view_ar],
    ["Remove Artist", remove_ar],
    ["Play Artist Songs", play_ar],
    ["Back"]
]

album_menu = [
    ["View Albums", view_al],
    ["Add Album", add_al],
    ["Remove Album", remove_al],
    ["play Album", play_al],
    ["Back"]
]

library_menu = [
    ["View Songs", view_lib],
    ["view Song", view_so],
    ["Add Song ", add_so],
    ["Remove Song", remove_so],
    ["Play Song with certain genre", play_gen],
    ["Back"]
]

meain_menu = [
    ["Playlists", exec_menu, playlist_menu],
    ["Artists", exec_menu, artist_menu],
    ["Albums", exec_menu, album_menu],
    ["Library", exec_menu, library_menu],
    ["Exit"]
]
##############################################
if __name__ == "__main__":
    autoplay_thread()
    exec_menu(meain_menu)
