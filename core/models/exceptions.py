class PlaylistDoesNotExists(Exception):
    pass


class PlaylistExists(Exception):
    pass


class UserNotAllowedToAddMorePlaylists(Exception):
    pass


class TrackDoesNotExist(Exception):
    pass


class UserNotAllowedToAddMoreTracksToPlaylist(Exception):
    pass


class UserDoesNotExist(Exception):
    pass


class MethodIsCorrupted(Exception):
    pass
