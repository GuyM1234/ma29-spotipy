from operator import itemgetter

from core.config import PATHS, DEFAULT_PREFERENCES, AUDIO_FEATURES
from core.models.user import get_user
from core.models.utils import read, get_track, get_user_tracks


def _get_recommended_value(track: dict, user_audio_profile: dict):
    return sum([abs(track['audio_profile'][audio_feature] - user_audio_profile[audio_feature]) for audio_feature in
                AUDIO_FEATURES]) / (track['popularity'] / 100)


def get_recommended_songs(username: str, number_of_songs: int, recommendation_func=_get_recommended_value):
    tracks = read(PATHS['tracks'])
    user_tracks = get_user_tracks(get_user(username))
    user_audio_profile = _calculate_audio_profile(user_tracks)
    songs = [(track['name'], track['popularity'], recommendation_func(track, user_audio_profile)) for track_id, track in
             tracks.items() if track_id not in user_tracks]
    return sorted(songs, key=itemgetter(2))[0:number_of_songs]


def _calculate_audio_profile(user_tracks: list):
    sum_audio_preferences = {audio_feature: 0 for audio_feature in AUDIO_FEATURES}
    for track_id in user_tracks:
        for audio_feature, value in get_track(track_id)['audio_profile'].items():
            sum_audio_preferences[audio_feature] += value

    return {audio_feature: value / len(user_tracks) for audio_feature, value in sum_audio_preferences.items()} \
        if len(user_tracks) > 0 else DEFAULT_PREFERENCES


