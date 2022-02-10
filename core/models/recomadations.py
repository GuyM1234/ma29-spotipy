from operator import itemgetter

from core.config import PATHS, DEFAULT_PREFERENCES, AUDIO_FEATURES
from core.models.user import get_user
from core.models.utils import read, get_track


def recommended_songs(username: str, number_of_songs: int):
    tracks = read(PATHS['tracks'])
    user_audio_profile = _calculate_audio_profile(get_user(username))
    songs = [(track['name'], track['popularity'], get_recommended_value(track, user_audio_profile)) for track in
             tracks.values()]
    return sorted(songs, key=itemgetter(2))[0:number_of_songs]


def _calculate_audio_profile(user: dict):
    sum_audio_preferences = {audio_feature: 0 for audio_feature in AUDIO_FEATURES}
    songs_number = 0
    for playlist in user['playlists']:
        songs_number += len(playlist)
        for track_id in playlist:
            for audio_feature, value in get_track(track_id)['audio_profile'].items():
                sum_audio_preferences[audio_feature] += value

    return {{audio_feature: value / songs_number} for audio_feature, value in sum_audio_preferences.items()} \
        if songs_number > 0 else DEFAULT_PREFERENCES


def get_recommended_value(track: dict, user_audio_profile: dict):
    return sum([abs(track['audio_profile'][audio_feature] - user_audio_profile[audio_feature]) for audio_feature in
                AUDIO_FEATURES])


print(recommended_songs('g', 5))
