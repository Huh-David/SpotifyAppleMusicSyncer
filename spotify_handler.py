import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import dotenv_values

from classes.Track import Track

config = dotenv_values('.env')  # create .env file

CLIENT_ID = config['SPOT_CLIENT_ID']
CLIENT_SECRET = config['SPOT_CLIENT_SECRET']
PLAYLIST_URI = config['SPOT_PLAYLIST_URI']


class SpotifyHandler(object):
    def __init__(self, client_id, client_secret):
        self.spotify = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials(
                client_id=client_id,
                client_secret=client_secret
            )
        )

    def get_tracks_from_playlist(self, playlist_uri: str) -> [Track]:
        results = self.spotify.playlist_items(playlist_uri)
        items = results['items']  # initialize list with values already in results

        while results['next']:  # iterate through all result sets and extend tracks by new result
            results = self.spotify.next(results)
            items.extend(results['items'])

        track_info_list = []
        tracks = []

        for item in items:
            track_info_list.append(item['track'])

        for track_info in track_info_list:
            track_name = track_info['name']
            track_artists = []
            for artist in track_info['artists']:
                track_artists.append(artist['name'])

            track = Track(
                name=track_name,
                artists=track_artists
            )

            tracks.append(track)

        return tracks


spotify_handler = SpotifyHandler(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)

print(spotify_handler.get_tracks_from_playlist(PLAYLIST_URI))
