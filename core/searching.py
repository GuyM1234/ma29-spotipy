from operator import itemgetter

from config import PATHS
from core.models import read


def get_artists():
    tracks = read(PATHS['tracks'])
    artists = set()
    for track in tracks.values():
        for artist in track['artists']:
            artists.add(artist['name'])


def get_artist_album(artist_id: str):
    tracks = read(PATHS['tracks'])
    return {track['album']['name'] for track in tracks.values() if
            artist_id in [artist['id'] for artist in track['artists']]}


def get_best_artist_songs(artist_id: str):
    tracks = read(PATHS['tracks'])
    songs = {(track['name'], track['popularity']) for track in tracks.values() if
             artist_id in [artist['id'] for artist in track['artists']]}
    return sorted(songs, key=itemgetter(1), reverse=True)


def get_album_songs(album_id: str):
    tracks = read(PATHS['tracks'])
    return {track['name'] for track in tracks.values() if track['album']['id'] == album_id}

