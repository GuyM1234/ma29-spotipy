import logging
from core.config import FREE, MAX_PLAYLIST_TRACKS_FOR_FREE_ACC, MAX_PLAYLISTS_FOR_FREE_ACC
from core.models.exceptions import PlaylistDoesNotExists, PlaylistExists, UserNotAllowedToAddMoreTracksToPlaylist, \
    UserNotAllowedToAddMorePlaylists
from core.models.user.general import get_user, _update_user
from core.models.utils import get_track


def get_playlist(user: dict, playlist_id):
    if user.get(playlist_id) is not None:
        return user.get(playlist_id)
    raise PlaylistDoesNotExists()


def _create_playlist_wrapper(func):
    def wrapper(username: str, playlist_name):
        user = get_user(username)
        if user['type'] == FREE and len(user['playlists']) == MAX_PLAYLISTS_FOR_FREE_ACC:
            raise UserNotAllowedToAddMorePlaylists()
        else:
            func(user, playlist_name)

    return wrapper


def _add_track_wrapper(func):
    def wrapper(username: str, playlist_id: str, track_id):
        user = get_user(username)
        playlist = get_playlist(user, playlist_id)  # raises error if playlists does not exist
        if user['type'] == FREE and len(playlist) == MAX_PLAYLIST_TRACKS_FOR_FREE_ACC:
            raise UserNotAllowedToAddMoreTracksToPlaylist()
        else:
            func(user, playlist_id, track_id)

    return wrapper


@_create_playlist_wrapper
def create_playlist(user: dict, playlist_id: str):
    if user['playlists'].get(playlist_id) is not None:
        logging.warning("Playlist exists")
        raise PlaylistExists()
    else:
        user['playlists'][playlist_id] = []
        _update_user(user)
        logging.info('Added playlist successfully')


@_add_track_wrapper
def add_track_to_playlist(user: dict, playlist_name: str, track_id: str):
    get_track(track_id)  # raises error if track does not exist
    user['playlists'][playlist_name].append(track_id)
    _update_user(user)
    logging.info('Added track successfully')


add_track_to_playlist("g", "guy 1", "asd")
