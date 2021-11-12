import applemusicpy
from dotenv import dotenv_values

from classes.Track import Track

config = dotenv_values('.env')  # create .env file

SECRET_KEY = config['AM_SECRET_KEY']
KEY_ID = config['AM_KEY_ID']
TEAM_ID = config['AM_TEAM_ID']
PLAYLIST_ID = config['AM_PLAYLIST_ID']


class AppleMusicHandler(object):
    def __init__(self, secret_key, key_id, team_id):
        self.apple_music = applemusicpy.AppleMusic(
            secret_key=secret_key,
            key_id=key_id,
            team_id=team_id
        )

    def get_tracks_from_playlist(self, playlist_id: str) -> [Track]:
        results = self.apple_music.playlist(playlist_id=playlist_id)

        tracks = []

        for item in results['data']:
            for track_info in item['relationships']['tracks']['data']:
                track_name = track_info['attributes']['name']
                track_artist = [
                    x for x in track_info['attributes']['artistName'].replace(' & ', ',').replace(', ', ',').split(',')
                ]

                track = Track(
                    name=track_name,
                    artists=track_artist
                )

                tracks.append(track)

        return tracks


apple_music_handler = AppleMusicHandler(
    secret_key=SECRET_KEY,
    key_id=KEY_ID,
    team_id=TEAM_ID
)

print(apple_music_handler.get_tracks_from_playlist(PLAYLIST_ID))
