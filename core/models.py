import os

from config import PATHS, FREE, logging, MAX_PLAYLISTS_FOR_FREE_ACC
from core.storage.readers import json_reader
from core.storage.writers import json_writer


def _add_doc_to_collection(path: str, doc: dict, id_field_name):
    collection = json_reader(path)
    collection[doc.pop(id_field_name)] = doc
    return collection


def read(file_path: str, reader=json_reader):
    return reader(file_path)


def write(path: str, doc: dict, id_field_name='id', writer=json_writer,
          add_doc_to_collection_method=_add_doc_to_collection):
    writer(path, add_doc_to_collection_method(path, doc, id_field_name))


def add_songs_folder():
    for song_path in os.listdir(PATHS['new_songs']):
        write(PATHS['tracks'], read(PATHS['new_songs'] + "\\" + song_path))
        logging.info("tracks uploaded")


def signup(username: str, password: str, user_type=FREE):
    write(PATHS['users'], {'username': username, 'password': password, 'type': user_type, 'playlists': {}}, 'username')


def login(username: str, password: str):
    users = read(PATHS['users'])
    if users.get(username) and users.get(username)['password'] == password:
        logging.info(f'{username} logged in successfully'.format(username=username))
        return True
    logging.info(f'{username} failed to log in'.format(username=username))
    return False




