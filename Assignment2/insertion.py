from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Song, Album, Artist, Playlist
from tinytag import TinyTag as tiny
from decimal import Decimal, getcontext
from pathlib import Path


engine = create_engine('sqlite:///Musicly.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_song(path):
    getcontext().prec = 3
    tag = tiny.get(path)
    artist = session.query(Artist).filter_by(name=tag.artist).first()
    if artist == None:
        artist = Artist(name=tag.artist)
        session.add(artist)
    album = session.query(Album).filter_by(name=tag.album).first()
    if album == None:
        album = Album(name=tag.album, num_songs=0, artist=artist)
        session.add(album)

    album.num_songs += 1
    duration = Decimal(tag.duration) / Decimal(60)
    song = Song(name=tag.title, release_date=tag.year,
                genre=tag.genre, length=duration, album=album, path=path)
    session.add(song)
    song.artists.append(artist)
    session.commit()


def add_album(path):
    pathlist = Path(path).glob('**/*.mp3')
    for i in pathlist:
        add_song(str(i))


def add_playlist(name, desc):
    playlist = Playlist(name=name, description=desc)
    session.add(playlist)
    session.commit()


def addto_playlist(playlist, song):
    song = session.query(Song).filter_by(name=song).first()
    playlist = session.query(Playlist).filter_by(name=playlist).first()
    if(playlist != None and song != None):
        playlist.songs.append(song)
        session.commit()


def add_album_to_playlist(playlist, album):
    playlist = session.query(Playlist).filter_by(name=playlist).first()
    album = session.query(Album).filter_by(name=album).first()
    if playlist != None and album != None:
        for song in album.songs:
            addto_playlist(playlist.name, song.name)


#add_song('Data\\Eminem - Kamikaze (2018) Mp3 (320kbps) [Hunter]\\01. The Ringer.mp3')
#add_album('Data\\Michael Jackson - Thriller 25 Super Deluxe Edition (2018)')
#add_playlist('Favs','listen to somethin new :)')
#add_album_to_playlist('Favs', 'Origins (Deluxe)')
#add_song('D:\\Serious Work\\Kolya\\Rab3a\\Concepts\\Assignment-2\\Data\\Imagine Dragons - Origins (Deluxe) (2018)\\07. Zero.mp3')
#path = str(input("Enter path: "))
# add_song(path)
