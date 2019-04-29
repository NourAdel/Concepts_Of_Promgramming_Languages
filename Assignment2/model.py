import os
import sys
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Table, create_engine

Base = declarative_base()


playlist_songs = Table('playlist_songs', Base.metadata,
                       Column('song_id', Integer, ForeignKey('song.id')),
                       Column('playlist_id', Integer,
                              ForeignKey('playlist.id'))
                       )

performers = Table('preformers', Base.metadata,
                   Column('song_id', Integer, ForeignKey('song.id')),
                   Column('artist_id', Integer, ForeignKey('artist.id'))
                   )


class Song(Base):
    __tablename__ = 'song'
    # Here we define columns for the table Song
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    release_date = Column(String(250))
    lyrics = Column(String(1000))
    genre = Column(String(250))
    length = Column(Float(precision=2))
    album_id = Column(Integer, ForeignKey('album.id'))
    path = Column(String(250), nullable=False)

    # relations
    playlists = relationship(
        'Playlist', secondary=playlist_songs, back_populates='songs', lazy='dynamic')
    artists = relationship('Artist', secondary=performers,
                           back_populates='songs', lazy='dynamic')


class Artist(Base):
    __tablename__ = 'artist'
    # Here we define columns for the table Artist.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    # relations
    songs = relationship(Song, secondary=performers,
                         back_populates='artists', lazy='dynamic')
    albums = relationship('Album', backref='artist')


class Album(Base):
    __tablename__ = 'album'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    num_songs = Column(Integer, nullable=False)
    artist_id = Column(Integer, ForeignKey('artist.id'))

    # relations
    songs = relationship(Song, backref='album', lazy='dynamic')


class Playlist(Base):
    __tablename__ = 'playlist'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(1000))
    
    # relations
    songs = relationship(Song, secondary=playlist_songs,
                         back_populates='playlists', lazy='dynamic')


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///Musicly.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)

