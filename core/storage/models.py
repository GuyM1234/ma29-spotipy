from core.storage.readers import json_reader
from core.storage.writers import json_writer


def add_track(read_from: str, write_to: str, reader=json_reader, writer=json_writer()):
    song = reader(read_from)



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