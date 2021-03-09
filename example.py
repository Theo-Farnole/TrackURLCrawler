from main import Main

track = "Talkie Walkie"
artist = "Nillie Winnie"

urls = Main.get_urls(track, artist)

print("Searching: " + track + " - " + artist)
print("\tYoutube: " + urls["youtube"])
print("\tSpotify: " + urls["spotify"])
print("\tDeezer: " + urls["deezer"])