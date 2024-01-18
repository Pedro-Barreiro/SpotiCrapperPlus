import googleapiclient.discovery


# List all videos from a youtube playlist
def listVideosFromYoutubePlaylist(youtubeServiceApi, playlistId):
    request = youtubeServiceApi.playlistItems().list(
        part="snippet,contentDetails", maxResults=25, playlistId=playlistId
    )

    try:
        response = request.execute()
    except googleapiclient.errors.HttpError as e:
        print(f"Failed to list videos from YouTube playlist: {e}")
        raise

    return response
