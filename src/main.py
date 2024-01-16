from dotenv import load_dotenv
import utils.spotify.index as spotify
import utils.youtube.index as youtube

load_dotenv()

def main():
    spotifyPlaylistId = '0dDRkPj44cUJHg0mq4etcK'

    # Scrape playlist from Spotify
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

    # Get playlists from YouTube
    try:
        youtubeServiceApi = youtube.getYoutubeOauth()
        youtubePlaylists = youtube.listYoutubePlaylists(youtubeServiceApi, playlist['playlist_name'])
    except Exception as e:
        print(f"Failed to check playlist on YouTube: {e}")
        return
    
    # Check if playlist already exists on YouTube
    ytPlaylistId = None
    for ytPlaylist in youtubePlaylists['items']:
        if ytPlaylist['snippet']['title'] == playlist['playlist_name']:
            ytPlaylistId = ytPlaylist['id']
            print("Playlist already exists on YouTube")
            break

    # If playlist does not exist on YouTube, create it
    if ytPlaylistId is None:
        try:
            youtubePlaylist = youtube.createYoutubePlaylist(youtubeServiceApi, playlist['playlist_name'])
            ytPlaylistId = youtubePlaylist['id']
            print("Created playlist on YouTube")
        except Exception as e:
            print(f"Failed to create playlist on YouTube: {e}")

    # Search for each track on YouTube
    for track in playlist['tracks']:
        try:
            youtubeVideo = youtube.searchYoutubeVideo(youtubeServiceApi, track['name'], track['artist'])
            youtubeVideoId = youtubeVideo['items'][0]['id']['videoId']
            print(f"Found video on YouTube: {youtubeVideoId}")
        except Exception as e:
            print(f"Failed to search video on YouTube: {e}")
            continue

        # Add video to playlist
        try:
            youtube.addVideoToYoutubePlaylist(youtubeServiceApi, ytPlaylistId, youtubeVideoId)
            print("Added video to playlist on YouTube")
        except Exception as e:
            print(f"Failed to add video to playlist on YouTube: {e}")

main()