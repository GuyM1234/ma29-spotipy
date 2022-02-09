from config import PATHS, logging, FREE, MAX_PLAYLISTS_FOR_FREE_ACC, MAX_PLAYLIST_TRACKS_FOR_FREE_ACC
from core.exceptions import PlaylistsExists, PlaylistDoesNotExists, UserNotAllowedToAddMoreTracksToPlaylist, \
    UserNotAllowedToAddMorePlaylists
from core.models import write, read


def _get_user(func):
    def wrapper(username: str, *args):
        user = read(PATHS['users']).get(username)
        user['username'] = username
        func(user, *args)

    return wrapper


def _create_playlist_wrapper(func):
    def wrapper(user: dict, playlist_name):
        if user['type'] == FREE and len(user['playlists'][playlist_name]) == MAX_PLAYLISTS_FOR_FREE_ACC:
            raise UserNotAllowedToAddMorePlaylists()
        else:
            func(user, playlist_name)

    return wrapper


def _add_track_wrapper(func):
    def wrapper(user: dict, *args):
        if user['type'] == FREE and len(user['playlists']) == MAX_PLAYLIST_TRACKS_FOR_FREE_ACC:
            raise UserNotAllowedToAddMoreTracksToPlaylist()
        else:
            func(user, *args)

    return wrapper


@_get_user
@_create_playlist_wrapper
def create_playlist(user: dict, playlist_name: str):
    if user['playlists'].get(playlist_name) is not None:
        logging.warning("Playlist exists")
        raise PlaylistsExists()
    else:
        user['playlists'][playlist_name] = []
        update_user(user)
        logging.info('Added playlist successfully')


@_get_user
def add_track_to_playlist(user: dict, playlist_name: str, track_id: str):
    if user['playlists'].get(playlist_name):
        user['playlists'][playlist_name].append(track_id)
        update_user(user)
        logging.info('Added track successfully')
    else:
        raise PlaylistDoesNotExists()


def update_user(user: dict):
    write(PATHS['users'], user, 'username')


create_playlist("asdbdsa", "13")
