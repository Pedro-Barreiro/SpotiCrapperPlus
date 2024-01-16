from dotenv import load_dotenv
import utils.spotify.index as spotify
import utils.youtube.index as youtube

load_dotenv()

def main():
    spotifyPlaylistId = '0dDRkPj44cUJHg0mq4etcK'

    try:
        spotifyAuth = spotify.getSpotifyAuth()
        playlist = spotify.scrape_playlist(spotifyAuth, spotifyPlaylistId)
        print("scraped playlist from Spotify")
    except Exception as e:
        print(f"Failed to scrape playlist from Spotify: {e}")
        return
    
    if not playlist:
        print("No playlist found on Spotify")
        return

    try:
        youtubeServiceApi = youtube.getYoutubeOauth()
        youtubePlaylists = youtube.listYoutubePlaylists(youtubeServiceApi, playlist['playlist_name'])
    except Exception as e:
        print(f"Failed to check playlist on YouTube: {e}")
        return
    
    ytPlaylistId = None
    for ytPlaylist in youtubePlaylists['items']:
        if ytPlaylist['snippet']['title'] == playlist['playlist_name']:
            ytPlaylistId = ytPlaylist['id']
            print("Playlist already exists on YouTube")
            break

    if ytPlaylistId is None:
        try:
            youtubePlaylist = youtube.createYoutubePlaylist(youtubeServiceApi, playlist['playlist_name'])
            ytPlaylistId = youtubePlaylist['id']
            print("Created playlist on YouTube")
        except Exception as e:
            print(f"Failed to create playlist on YouTube: {e}")

main()