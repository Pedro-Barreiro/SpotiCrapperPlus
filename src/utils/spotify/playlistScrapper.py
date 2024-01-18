import spotipy


# Scrape a playlist
def scrape_playlist(spotify, playlist_id):
    try:
        results = spotify.playlist(playlist_id)
    except spotipy.client.SpotifyException as e:
        print(f"Failed to scrape playlist on Spotify: {e}")
        raise

    playlistTracks = results["tracks"]["items"]
    tracks = []

    for track in playlistTracks:
        track_name = track["track"]["name"]
        artist_name = track["track"]["artists"][0]["name"]
        track_info = {"name": track_name, "artist": artist_name}
        tracks.append(track_info)

    playlist = {"type": "playlist", "playlist_name": results["name"], "tracks": tracks}

    return playlist
