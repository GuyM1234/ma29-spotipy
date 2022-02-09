import os
from config import PATHS, logging
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
    writer(path, add_doc_to_collection_method(path, doc, id_field_name))


def add_songs_folder():
    for song_path in os.listdir(PATHS['new_songs']):
        write(PATHS['tracks'], read(PATHS['new_songs'] + "\\" + song_path))
        logging.info("tracks uploaded")







