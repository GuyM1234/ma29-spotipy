class PlaylistDoesNotExists(Exception):
    pass


class PlaylistsExists(Exception):
    pass


class UserNotAllowedToAddMorePlaylists(Exception):
    pass


class TrackDoesNotExist(Exception):
    pass


class UserNotAllowedToAddMoreTracksToPlaylist(Exception):
    pass


class UsernameDoesNotExist(Exception):
    pass


class MethodIsCorrupted(Exception):
    pass
