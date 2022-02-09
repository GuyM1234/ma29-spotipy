
from config import PATHS


def write_track_to_db(song):
    pass


def add_track(read_from: str, reader=json_reader, writer=write_track_to_db):
    track = reader(read_from)
    print(track)

{
    "artist_id": {
        "name": "",
        "albums": ["id", "id"]
    }
}

{
    "album_id": {
        "name": "",
        "songs": []
    }
}

{
    "song_id": {
        "name": "guy",
        "popular": ""
    }
}
