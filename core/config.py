import logging

PATHS = {
    "tracks": r"C:\Users\user\Desktop\Code\ma29-spotipy\db\tracks.json",
    "users": r"C:\Users\user\Desktop\Code\ma29-spotipy\db\users.json",
    "new_songs": r"C:\Users\user\Desktop\Code\ma29-spotipy\songs",
    "audio_features": r"C:\Users\user\Desktop\Code\ma29-spotipy\audio_features",
    "log_file": r"C:\Users\user\Desktop\Code\ma29-spotipy\db\log.txt",
}
FREE = "free"
PREMIUM = "premium"
logging.basicConfig(filename=PATHS['log_file'], encoding='utf-8', level=logging.DEBUG)
MAX_PLAYLISTS_FOR_FREE_ACC = 5
MAX_PLAYLIST_TRACKS_FOR_FREE_ACC = 20
AUDIO_FEATURES = {"danceability", "energy", "acousticness", "instrumentalness", "valence"}
DEFAULT_PREFERENCES = {audio_feature: 0.5 for audio_feature in AUDIO_FEATURES}
