import googleapiclient.discovery


# Search YouTube video
def searchYoutubeVideo(youtubeServiceApi, trackName, artistName):
    request = youtubeServiceApi.search().list(
        part="snippet", maxResults=1, q=f"{trackName} - {artistName}", type="video"
    )
    try:
        response = request.execute()
    except googleapiclient.errors.HttpError as e:
        print(f"Failed to search YouTube video: {e}")
        raise

    return response
