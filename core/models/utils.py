import os
from core.config import PATHS, logging
from core.models.exceptions import TrackDoesNotExist
from core.storage.readers import json_reader
from core.storage.writers import json_writer


def _add_doc_to_collection(path: str, doc: dict, id_field_name):
    collection = json_reader(path)
    collection[doc.pop(id_field_name)] = doc
    return collection


def read(file_path: str, reader: object = json_reader) -> dict:
    return reader(file_path)


def write(path: str, doc: dict, id_field_name='id', writer=json_writer,
          add_doc_to_collection_method=_add_doc_to_collection):
    doc = add_doc_to_collection_method(path, doc, id_field_name) if add_doc_to_collection_method is not None else doc
    writer(path, doc)


def add_songs():
    for song_path in os.listdir(PATHS['new_songs']):
        write(PATHS['tracks'], read(PATHS['new_songs'] + "\\" + song_path))
    logging.info("{len} tracks uploaded".format(len=len(os.listdir(PATHS['new_songs']))))


def add_audio_features():
    tracks = read(PATHS['tracks'])
    for audio_feature_path in os.listdir(PATHS['audio_features']):
        audio_feature = read(PATHS['audio_features'] + "\\" + audio_feature_path)
        tracks[audio_feature.pop('id')]['audio_profile'] = audio_feature
    write(PATHS['tracks'], tracks, add_doc_to_collection_method=None)
    logging.info("Tracks updated")


def get_track(track_id):
    tracks = read(PATHS['tracks'])
    if tracks.get(track_id):
        return tracks[track_id]
    raise TrackDoesNotExist


def get_user_tracks(user: dict):
    return sum(user['playlists'].values(), [])
