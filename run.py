from youtubeURL import YoutubeURL
from spotifyURL import SpotifyURL
from deezerURL import DeezerURL

track = "Tout"
artist = "Squeezie"

ytURL = YoutubeURL.get_youtube_url(track, artist)
spURL = SpotifyURL.get_spotify_url(track, artist)
dzURL = DeezerURL.get_deezer_url(track, artist)

print("Searching: " + track + " - " + artist)
print("\tYoutube: " + ytURL)
print("\tSpotify: " + spURL)
print("\tDeezer: " + dzURL)

