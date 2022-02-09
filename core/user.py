from config import PATHS, MAX_PLAYLISTS_FOR_FREE_ACC, logging, FREE
from core.models import write, read


class User:
    @staticmethod
    def authenticate(username, func):
        def wrapper(name: str):
            if self.user['type'] == FREE and len(self.user['playlists']) == MAX_PLAYLISTS_FOR_FREE_ACC:
                logging.info('User is not allowed to create more playlists')
            else:
                func(name)

        return wrapper

    @staticmethod
    @authenticate
    def create_playlist(name: str):
        if self.user['playlists'].get(name):
            logging.info('{username} tried to create a playlist that exists'.format(username=self.user))
        else:
            self.user['playlists'][name] = []

    @staticmethod
    def add_track_to_playlist(playlist_name, track_id):
        pass

    def update_user(user: dict):
        write(PATHS['users'], user, 'username')

    @staticmethod
    def get_user(username):
        return read([PATHS.read])