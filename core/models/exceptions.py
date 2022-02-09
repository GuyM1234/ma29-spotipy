class PlaylistDoesNotExists(Exception):
    pass


class PlaylistsExists(Exception):
    pass


class UserNotAllowedToAddMorePlaylists(Exception):
    pass


class TrackDoesNotExists(Exception):
    pass


class UserNotAllowedToAddMoreTracksToPlaylist(Exception):
    pass
