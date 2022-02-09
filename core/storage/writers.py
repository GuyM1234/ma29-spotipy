import json


def json_writer(file_path: str, data: dict):
    with open(file_path, "w") as new_file:
        new_file.write(str(json.dumps(data)))


json_writer(r"..\..\db\albums\hey_yo.json", {"hi": "yo"})
