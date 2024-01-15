import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()

# Set up your Spotify API credentials
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

# Authenticate with Spotify API
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Scrape a playlist
def scrape_playlist(playlist_id):
    results = sp.playlist(playlist_id)
    playlistTracks = results['tracks']['items']
    tracks = []

    for track in playlistTracks:
        track_name = track['track']['name']
        artist_name = track['track']['artists'][0]['name']
        track_info = {
            'name': track_name,
            'artist': artist_name
        }
        tracks.append(track_info)

    playlist = {
        'playlist_name': results['name'],
        'tracks': tracks
    }

    return playlist

# Scrape an album
def scrape_album(album_id):
    results = sp.album(album_id)
    tracks = results['tracks']['items']

    album = {
        'album_name': results['name'],
        'artist_name': results['artists'][0]['name'],
        'tracks': [track['name'] for track in tracks]
    }

    return album

# Example usage
playlist_id = '37i9dQZF1DX0rV7skaITBo'
playlist = scrape_playlist(playlist_id)
print(f"---\nPlaylist: {playlist['playlist_name']}")
print("Tracks:")
for track in playlist['tracks']:
    print(f"- {track['name']} by {track['artist']}")

album_id = '4chPUBJXFpxBagtuD5l0rq'
album = scrape_album(album_id)
print(f"---\nAlbum: {album['album_name']}")
print(f"Artist: {album['artist_name']}")
print("Tracks:")
for track in album['tracks']:
    print(f"- {track}")