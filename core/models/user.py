from core.config import PATHS, logging, FREE, MAX_PLAYLISTS_FOR_FREE_ACC, MAX_PLAYLIST_TRACKS_FOR_FREE_ACC
from core.models.exceptions import PlaylistsExists, PlaylistDoesNotExists, UserNotAllowedToAddMoreTracksToPlaylist, \
    UserNotAllowedToAddMorePlaylists, UsernameDoesNotExist, UserDoesNotExist
from core.models.utils import write, read, get_track


def _get_user(func):
    def wrapper(username: str, *args):
        if read(PATHS['users']).get(username) is not None:
            user = read(PATHS['users']).get(username)
            user['username'] = username
            return func(user, *args)
        raise UserDoesNotExist()

    return wrapper


@_get_user
def get_user(user: dict):
    return user


def _create_playlist_wrapper(func):
    def wrapper(user: dict, playlist_name):
        if user['type'] == FREE and len(user['playlists']) == MAX_PLAYLISTS_FOR_FREE_ACC:
            raise UserNotAllowedToAddMorePlaylists()
        else:
            func(user, playlist_name)

    return wrapper


def _add_track_wrapper(func):
    def wrapper(user: dict, playlist_name):
        if user['type'] == FREE and len(user['playlists'][playlist_name]) == MAX_PLAYLIST_TRACKS_FOR_FREE_ACC:
            raise UserNotAllowedToAddMoreTracksToPlaylist()
        else:
            func(user, playlist_name)

    return wrapper


@_get_user
@_create_playlist_wrapper
def create_playlist(user: dict, playlist_name: str):
    if user['playlists'].get(playlist_name) is not None:
        logging.warning("Playlist exists")
        raise PlaylistsExists()
    else:
        user['playlists'][playlist_name] = []
        _update_user(user)
        logging.info('Added playlist successfully')


@_get_user
def add_track_to_playlist(user: dict, playlist_name: str, track_id: str):
    if user['playlists'].get(playlist_name) is not None:
        get_track(track_id)  # raises error if track does not exist
        user['playlists'][playlist_name].append(track_id)
        _update_user(user)
        logging.info('Added track successfully')
    else:
        raise PlaylistDoesNotExists()


def login(username: str, password: str):
    users = read(PATHS['users'])
    if users.get(username) and users.get(username)['password'] == password:
        logging.info(f'{username} logged in successfully'.format(username=username))
    logging.info(f'{username} failed to log in'.format(username=username))
    raise UserDoesNotExist()


def signup(username: str, password: str, user_type=FREE):
    new_user = {'username': username, 'password': password, 'type': user_type, 'playlists': {}}
    write(PATHS['users'], new_user, 'username')


def _update_user(user: dict):
    write(PATHS['users'], user, 'username')
