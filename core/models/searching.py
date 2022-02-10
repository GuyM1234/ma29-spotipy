from operator import itemgetter

from core.config import PATHS, FREE, AUDIO_FEATURES
from core.models.exceptions import MethodIsCorrupted
from core.models.models import read
from core.models.user import get_user


def authenticate(func):
    def wrapper(username, *args):
        result = func(*args)
        return list(result)[0:5] if get_user(username)['type'] == FREE else result

    return wrapper


@authenticate
def get_artists():
    tracks = read(PATHS['tracks'])
    artists = set()
    for track in tracks.values():
        for artist in track['artists']:
            artists.add(artist['name'])

    return artists


@authenticate
def get_artist_album(artist_id: str):
    tracks = read(PATHS['tracks'])
    return {track['album']['name'] for track in tracks.values() if
            artist_id in [artist['id'] for artist in track['artists']]}


@authenticate
def get_best_artist_songs(artist_id: str):
    tracks = read(PATHS['tracks'])
    songs = {(track['name'], track['popularity']) for track in tracks.values() if
             artist_id in [artist['id'] for artist in track['artists']]}
    return sorted(songs, key=itemgetter(1), reverse=True)


@authenticate
def get_album_songs(album_id: str):
    tracks = read(PATHS['tracks'])
    return {track['name'] for track in tracks.values() if track['album']['id'] == album_id}


# template for more searching methods
@authenticate
def user_created_searching_method(func, *args):
    tracks = read(PATHS['tracks'])
    try:
        return func(tracks, *args)
    except Exception:
        raise MethodIsCorrupted()


# @authenticate
def recommended_songs(user_audio_profile: dict):
    tracks = read(PATHS['tracks'])
    songs = [(track['name'], track['popularity'], get_recommended_value(track, user_audio_profile)) for track in tracks.values()]
    return sorted(songs, key=itemgetter(2))


def get_recommended_value(track, user_audio_profile):
    return sum([abs(track['audio_profile'][audio_feature] - user_audio_profile[audio_feature]) for audio_feature in AUDIO_FEATURES])


print(recommended_songs(r))
