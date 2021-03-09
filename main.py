from youtubeURL import YoutubeURL
from spotifyURL import SpotifyURL
from deezerURL import DeezerURL

class Main:
    def get_urls(track, artist):
        ytURL = YoutubeURL.get_youtube_url(track, artist)
        spURL = SpotifyURL.get_spotify_url(track, artist)
        dzURL = DeezerURL.get_deezer_url(track, artist)

        output = {
            "youtube" : ytURL,
            "spotify" : spURL,
            "deezer" : dzURL
        }

        return output

