class Artist:
    def __init__(self, name: str, albums=[], singles=[]):
        self._name = name
        self._albums = albums
        self._singles = singles

    def add_album(self, album_id: str):
        self._albums.append(album_id)

    def add_single(self, song_id: str):
        self._singles.append(song_id)
