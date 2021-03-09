import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyURL:
    def get_spotify_url(track, artist):
        searchQuery = str.format("artist:{0} track:{1}" , artist, track)

        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())
        results = sp.search(q=searchQuery, limit=1, type='track')

        url = results["tracks"]["items"][0]["external_urls"]["spotify"]
        return url