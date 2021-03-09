import deezer

class DeezerURL:
    def get_deezer_url(track, artist):
            client = deezer.Client()
            searchQuery = {
                "artist": artist,
                "track" : track,                
            }
            searches = client.advanced_search(searchQuery, relation="track")

            return searches[0].link