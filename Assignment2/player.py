from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Song, Album, Artist, Playlist
from pygame import mixer as player
import pygame
import threading
import random
from os import system

# DB session
engine = create_engine('sqlite:///Musicly.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#global variables
player.init()
ind = 0
list_songs = []
paused = False
playing = False
order = ''
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


def autoplay():
    while True:
        if not player.music.get_busy() and playing:
            play_next()


def autoplay_thread():
    threading1 = threading.Thread(target=autoplay)
    threading1.daemon = True
    threading1.start()


def handler():
    global paused, ind, playing
    playing = True
    while True:
        system('cls')
        print(colorize(header, 'pink'))
        print(colorize('version 0.1\n', 'green'))
        print("\n1 - Pause/Resume\n2 - Next\n3 - Quit\n")
        option = input("Enter an option: ")
        if option == '1':
            if not paused:
                player.music.pause()
                paused = True
            else:
                player.music.unpause()
                paused = False
        elif option == '2':
            player.music.stop()
            paused = False
        elif option == '3':
            player.music.stop()
            ind = 0
            playing = False
            break
        else:
            continue


def play_next():
    global ind, order
    if order == 'normal':
        player.music.load(list_songs[ind])
        player.music.play()
        if ind == len(list_songs)-1:
            ind = -1
        ind += 1
    else:
        rand = random.randint(0, len(list_songs)-1)
        while ind == rand:
            rand = random.randint(0, len(list_songs)-1)
        ind = rand
        player.music.load(list_songs[ind])
        player.music.play()


def play_album(name):
    global list_songs, order
    order = 'normal'
    album = session.query(Album).filter_by(name=name).first()
    if(album != None):
        list_songs = [song.path for song in album.songs]
        handler()


def play_artist(name):
    global list_songs, order
    order = 'normal'
    artist = session.query(Artist).filter_by(name=name).first()
    if(artist != None):
        list_songs = [song.path for song in artist.songs]
        handler()


def play_songs(genre):
    global list_songs, order
    order = 'normal'
    songs = session.query(Song).filter_by(genre=genre).all()
    if songs != None:
        list_songs = [song.path for song in songs]
        handler()


def play_playlist(name, ord):
    global list_songs, order
    playlist = session.query(Playlist).filter(Playlist.name == name).first()
    if playlist != None:
        if ord == '1':
            list_songs = [
                song.path for song in playlist.songs.order_by(Song.name.asc())]
            order = 'normal'
        elif ord == '2':
            list_songs = [
                song.path for song in playlist.songs.order_by(Song.name.desc())]
            order = 'normal'
        elif ord == '3':
            list_songs = [
                song.path for song in playlist.songs.order_by(Song.album_id)]
            order = 'normal'
        elif ord == '4':
            list_songs = [
                song.path for song in playlist.songs.order_by(Song.genre)]
            order = 'normal'
        elif ord == '5':
            list_songs = [
                song.path for song in playlist.songs.order_by(Song.release_date)]
            order = 'normal'
        elif ord == '6':
            list_songs = [song.path for song in playlist.songs]
            order = 'shuffle'
        handler()


# autoplay_thread()
# play_artist('Eminem')
#play_playlist('Favs', 'shuffle')
#play_album('Origins (Deluxe)')
# play_songs('Hip-Hop/Rap')
