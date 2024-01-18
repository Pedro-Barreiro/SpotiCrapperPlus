import utils.spotify.index as spotify
import utils.menu.index as menu
from main import main


def choice1():
    # 0dDRkPj44cUJHg0mq4etcK
    spotifyPlaylistId = input("Enter Spotify playlist ID: ")

    # Scrape playlist from Spotify
    try:
        spotifyAuth = spotify.getSpotifyAuth()
        playlist = spotify.scrape_playlist(spotifyAuth, spotifyPlaylistId)
        print("Scraped playlist from Spotify")

        menu.spotifyPostActionMenu(playlist)
    except Exception as e:
        print(f"Failed to scrape playlist from Spotify: {e}")
        main()


def choice2():
    spotifyAlbumId = input("Enter Spotify album ID: ")

    # Scrape album from Spotify
    try:
        spotifyAuth = spotify.getSpotifyAuth()
        album = spotify.scrape_album(spotifyAuth, spotifyAlbumId)
        print("Scraped album from Spotify")

        menu.spotifyPostActionMenu(album)
    except Exception as e:
        print(f"Failed to scrape album from Spotify: {e}")
        main()
