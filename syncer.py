from handlers.apple_music_handler import AppleMusicHandler
from handlers.spotify_handler import SpotifyHandler

from dotenv import dotenv_values

config = dotenv_values('.env')

AM_SECRET_KEY = config['AM_SECRET_KEY']
AM_KEY_ID = config['AM_KEY_ID']
AM_TEAM_ID = config['AM_TEAM_ID']
AM_PLAYLIST_ID = config['AM_PLAYLIST_ID']

SPOT_CLIENT_ID = config['SPOT_CLIENT_ID']
SPOT_CLIENT_SECRET = config['SPOT_CLIENT_SECRET']
SPOT_PLAYLIST_URI = config['SPOT_PLAYLIST_URI']
SPOT_PLAYLIST_ID = config['SPOT_PLAYLIST_ID']
SPOT_USER_ID = config['SPOT_USER_ID']


class Syncer(object):
    def __init__(self, spotify_handler: SpotifyHandler, apple_music_handler: AppleMusicHandler):
        self.spotify_handler = spotify_handler
        self.apple_music_handler = apple_music_handler

    def sync_to_spotify(self, am_playlist_id, spot_user, spot_playlist_name, spot_playlist_id=None):
        tracks = self.apple_music_handler.get_tracks_from_playlist(playlist_id=am_playlist_id)

        if spot_playlist_id is None:
            spot_playlist_id = self.spotify_handler.create_playlist(user=spot_user, name=spot_playlist_name)
        else:
            self.spotify_handler.clear_playlist(playlist_id=spot_playlist_id)
            self.spotify_handler.update_playlist_description(playlist_id=spot_playlist_id)

        self.spotify_handler.add_tracks_to_playlist(playlist_id=spot_playlist_id, tracks=tracks)


def main():
    apple_music_handler = AppleMusicHandler(
        secret_key=AM_SECRET_KEY,
        key_id=AM_KEY_ID,
        team_id=AM_TEAM_ID
    )
    spotify_handler = SpotifyHandler(
        client_id=SPOT_CLIENT_ID,
        client_secret=SPOT_CLIENT_SECRET
    )
    syncer = Syncer(
        spotify_handler=spotify_handler,
        apple_music_handler=apple_music_handler
    )

    name_of_playlist = 'Sweet Dreams'

    syncer.sync_to_spotify(
        am_playlist_id=AM_PLAYLIST_ID,
        spot_user=SPOT_USER_ID,
        spot_playlist_name=name_of_playlist,
        spot_playlist_id=SPOT_PLAYLIST_ID
    )


if __name__ == '__main__':
    main()
