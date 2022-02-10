from operator import itemgetter
from typing import Iterable

from core.config import PATHS, FREE, MAX_SEARCH_RESULT_FOR_FREE_ACC
from core.models.exceptions import MethodIsCorrupted
from core.models.user.utils import get_user
from core.models.utils import read


def authenticate(result: Iterable, username: str):
    return list(result)[0:MAX_SEARCH_RESULT_FOR_FREE_ACC] if get_user(username)['type'] == FREE else result


def get_artists(username: str):
    tracks = read(PATHS['tracks'])
    artists = set()
    for track in tracks.values():
        for artist in track['artists']:
            artists.add(artist['name'])

    return authenticate(artists, username)


def get_artist_album(username: str, artist_id: str):
    tracks = read(PATHS['tracks'])
    albums = {track['album']['name'] for track in tracks.values() if
              artist_id in [artist['id'] for artist in track['artists']]}
    return authenticate(albums, username)


def get_best_artist_songs(username: str, artist_id: str):
    tracks = read(PATHS['tracks'])
    songs = {(track['name'], track['popularity']) for track in tracks.values()
             if artist_id in [artist['id'] for artist in track['artists']]}
    return authenticate(sorted(songs, key=itemgetter(1), reverse=True), username)


def get_album_songs(username: str, album_id: str):
    tracks = read(PATHS['tracks'])
    songs = {track['name'] for track in tracks.values() if track['album']['id'] == album_id}
    return authenticate(songs, username)


# template for more searching methods
def generic_search_method(func, *args):
    tracks = read(PATHS['tracks'])
    try:
        return authenticate(func(tracks, *args))
    except Exception:
        raise MethodIsCorrupted()
