import json


def json_reader(file_path: str):
    with open(file_path, "r") as new_file:
        return json.load(new_file)
