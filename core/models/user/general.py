from core.config import PATHS, logging, FREE, MAX_PLAYLISTS_FOR_FREE_ACC, MAX_PLAYLIST_TRACKS_FOR_FREE_ACC
from core.models.exceptions import PlaylistExists, PlaylistDoesNotExists, UserNotAllowedToAddMoreTracksToPlaylist, \
    UserNotAllowedToAddMorePlaylists, UserDoesNotExist
from core.models.utils import write, read, get_track


def get_user(username: str):
    if read(PATHS['users']).get(username) is not None:
        user = read(PATHS['users']).get(username)
        user['username'] = username
        return user
    raise UserDoesNotExist()


def _update_user(user: dict):
    write(PATHS['users'], user, 'username')


def login(username: str, password: str):
    users = read(PATHS['users'])
    if users.get(username) and users.get(username)['password'] == password:
        logging.info(f'{username} logged in successfully'.format(username=username))
    else:
        logging.info(f'{username} failed to log in'.format(username=username))
        raise UserDoesNotExist()


def signup(username: str, password: str, user_type=FREE):
    new_user = {'username': username, 'password': password, 'type': user_type, 'playlists': {}}
    write(PATHS['users'], new_user, 'username')



