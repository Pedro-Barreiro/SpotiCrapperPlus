import utils.spotify.index as spotify
from main import main

def mainMenuHandler(choice):
    if choice == "1":
        # 0dDRkPj44cUJHg0mq4etcK
        spotifyPlaylistId = input("Enter Spotify playlist ID: ")

         # Scrape playlist from Spotify
        playlist = None
        try:
            spotifyAuth = spotify.getSpotifyAuth()
            playlist = spotify.scrape_playlist(spotifyAuth, spotifyPlaylistId)
            print("Scraped playlist from Spotify")
        except Exception as e:
            print(f"Failed to scrape playlist from Spotify: {e}")
        
        if playlist == None:
            print("No playlist found on Spotify")
            main()
            
    elif choice == "2":
        spotifyAlbumId = input("Enter Spotify album ID: ")
    elif choice == "3":
        print("Exiting...")
        exit()
    else:
        print("Invalid choice!")
        main()