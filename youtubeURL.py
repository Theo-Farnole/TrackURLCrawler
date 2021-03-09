from youtube_search import YoutubeSearch

class YoutubeURL:
    def get_youtube_url(track, artist):    
        searchQuery = artist + " " + track
        ytResults = YoutubeSearch(searchQuery,max_results=1).to_dict()
        ytURL = "https://www.youtube.com" + ytResults[0]["url_suffix"]
        return ytURL