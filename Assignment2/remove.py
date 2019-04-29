from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Song, Album, Artist, Playlist, performers


engine = create_engine('sqlite:///Musicly.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def Delete_Song(Name):
    s = session.query(Song).filter(Song.name == Name).first()
    if(s != None):
        s.album.num_songs -= 1
        if(s.album.num_songs <= 0):
            session.delete(s.album)
        for artist in s.artists:
            if(artist.songs.count()-1 == 0):
                session.delete(artist)
        session.delete(s)
        session.commit()


def Delete_Playlist(Name):
    for p in session.query(Playlist).filter(Playlist.name == Name):
        session.delete(p)
        session.commit()


def Delete_Album(Name):
    for album in session.query(Album).filter(Album.name == Name):
        for song in album.songs:
            Delete_Song(song.name)
        session.commit()


def Delete_Artist(name):
    artist = session.query(Artist).filter(Artist.name == name).first()
    if artist != None:
        for song in artist.songs:
            Delete_Song(song.name)
        session.commit()


def DeleteFrom_Playlist(Pname, Sname):
    for p in session.query(Playlist).filter(Playlist.name == Pname):
        for s in session.query(Song).filter(Song.name == Sname):
            p.songs.remove(s)
            session.commit()


#Delete_Album('Kamikaze')
# Delete_Song('Normal')
#Delete_Album('Thriller 25 (Super Deluxe Edition)')
# Delete_Playlist('menna3beta')
#DeleteFrom_Playlist('Favs', 'Kamikaze')
#Delete_Artist('Vincent Price')