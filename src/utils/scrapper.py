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
    playlist_name = results['name']
    tracks = results['tracks']['items']
    
    print(f"Playlist Name: {playlist_name}")
    print("Tracks:")
    for track in tracks:
        track_name = track['track']['name']
        artist_name = track['track']['artists'][0]['name']
        print(f"- {track_name} by {artist_name}")

# Example usage
playlist_id = '37i9dQZF1DX0rV7skaITBo'
playlist = scrape_playlist(playlist_id)
print(playlist)