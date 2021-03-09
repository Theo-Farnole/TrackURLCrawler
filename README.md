# Track URLs Getter

## Supported platforms

- Youtube (not Youtube Music)
- Spotify
- Deezer

## Installation

[Spotipy](https://spotipy.readthedocs.io/en/2.17.1/#installation)
[Youtube Search](https://pypi.org/project/youtube-search/)
[Deezer](https://pypi.org/project/deezer-python/)

```python
pip install spotipy
pip install youtube-search
pip install deezer-python
```

## Usage

```python
urls = Main.get_urls("Talkie Walkie", "Nillie Winnie")
urls["youtube"] # get youtube URL
urls["spotify"] # get spotify URL
urls["deezer"] # get deezer URL
```

