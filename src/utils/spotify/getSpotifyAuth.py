import os
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy


def getSpotifyAuth():
    # Set up your Spotify API credentials
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    # Authenticate with Spotify API
    client_credentials_manager = SpotifyClientCredentials(
        client_id=client_id, client_secret=client_secret
    )
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    return spotify
