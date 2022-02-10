from core.models.searching import get_album_songs
from flask import Flask, request, jsonify

from core.models import get_recommended_songs, get_artists, get_artist_album, get_best_artist_songs

app = Flask(__name__)


@app.route('/all_artists', methods=["POST"])
def all_artists():
    return jsonify(get_artists(request.form.to_dict()['username']))


@app.route('/artist_albums', methods=["POST"])
def artist_albums():
    return jsonify(get_artist_album(request.form.to_dict()['username'], request.form.to_dict()['id']))


@app.route('/best_artist_songs', methods=["POST"])
def best_artist_songs():
    return jsonify(get_best_artist_songs(request.form.to_dict()['username'], request.form.to_dict()['id']))


@app.route('/album_songs', methods=["POST"])
def album_songs():
    return jsonify(get_album_songs(request.form.to_dict()['username'], request.form.to_dict()['id']))


@app.route('/recommended_songs', methods=["POST"])
def recommended_songs():
    return jsonify(get_recommended_songs(request.form.to_dict()['username'], int(request.form.to_dict()['song_number'])))


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
