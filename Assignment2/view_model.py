from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Song, Album, Artist, Playlist


engine = create_engine('sqlite:///Musicly.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def view_playlists():
    print()
    for playlist in session.query(Playlist).all():
        print('* {0:30}  Tracks:{1:3d}'.format(playlist.name,
                                               playlist.songs.count()))
    input("\nPress [Enter] to continue...")


def view_playlist(name, order):
    for p in session.query(Playlist).filter(Playlist.name == name):
        print('\nName: {0:25}'.format(p.name))
        print('Descreption: {0:50}'.format(p.description))
        print("\nSongs:")

        # view by specific order
        if order == '1':
            for s in p.songs.order_by(Song.name.asc()):
                print(" -{0:40}  Duration: {1:4}".format(s.name, s.length))
        elif order == '2':
            for s in p.songs.order_by(Song.name.desc()):
                print(" -{0:40}  Duration: {1:4}".format(s.name, s.length))
        elif order == '3':
            for s in p.songs.order_by(Song.album_id):
                print(" -{0:40}  Duration: {1:4}".format(s.name, s.length))
        elif order == '4':
            for s in p.songs.order_by(Song.genre):
                print(" -{0:40}  Duration: {1:4}".format(s.name, s.length))
        elif order == '5':
            for s in p.songs.order_by(Song.release_date):
                print(" -{0:40}  Duration: {1:4}".format(s.name, s.length))


def view_albums():
    albums = session.query(Album).all()
    if(albums != None):
        print()
        for album in albums:
            print('* {0:30}  Tracks:{1:3d}'.format(album.name, album.songs.count()))


def view_artists():
    artists = session.query(Artist).all()
    if(artists != None):
        print()
        for artist in artists:
            print(f'* {artist.name}')


def view_songs():
    songs = session.query(Song).all()
    for i in range(len(songs)):
        if(i % 4 == 0 and i != 0):
            print()
        print('- {0:40}'.format(songs[i].name), end='')


def view_song(name):
    for s in session.query(Song).filter(Song.name == name):
        print()
        print('  Song: {0:30}'.format(s.name))
        for artist in s.artists:
            print("  Artists: {0:30}".format(artist.name))
            for i in session.query(Album).filter(Album.id == s.album_id):
                print('  Album: {0:30}'.format(i.name))
                print('  Genre: {0:15}'.format(s.genre))
                print("  Release Date: {0:10}".format(s.release_date))


# view_playlists()
# view_albums()
# view_artists()
# view_songs()
#view_playlist('menna3beta', 'album')
# view_song('Greatest')
