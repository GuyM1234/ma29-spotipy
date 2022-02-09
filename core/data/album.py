class Album:
    def __init__(self, name: str, songs=[]):
        self._name = name
        self._songs = songs

    def add_song(self, song_id: str):
        self._songs.append(song_id)

