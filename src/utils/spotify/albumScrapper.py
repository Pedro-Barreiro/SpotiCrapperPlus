import spotipy

# Scrape an album
def scrape_album(spotify, album_id):
    try:
        results = spotify.album(album_id)
    except spotipy.client.SpotifyException as e:
        print(f"Failed to scrape album on Spotify: {e}")
        raise
    
    tracks = results['tracks']['items']

    album = {
        'album_name': results['name'],
        'artist_name': results['artists'][0]['name'],
        'tracks': [track['name'] for track in tracks]
    }

    return album

# Example usage
# album_id = '4chPUBJXFpxBagtuD5l0rq'
# album = scrape_album(album_id)
# print(f"---\nAlbum: {album['album_name']}")
# print(f"Artist: {album['artist_name']}")
# print("Tracks:")
# for track in album['tracks']:
#     print(f"- {track}")