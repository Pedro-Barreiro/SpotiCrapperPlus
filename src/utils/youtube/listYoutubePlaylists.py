import googleapiclient.discovery


# List YouTube playlists
def listYoutubePlaylists(youtubeServiceApi, playlistName):
    request = youtubeServiceApi.playlists().list(
        part="snippet,contentDetails", maxResults=100, mine=True
    )
    try:
        response = request.execute()
    except googleapiclient.errors.HttpError as e:
        print(f"Failed to check playlist on YouTube: {e}")
        raise

    return response
