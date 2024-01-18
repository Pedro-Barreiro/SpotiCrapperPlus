import googleapiclient.discovery


# Create YouTube playlist
def createYoutubePlaylist(youtubeServiceApi, playlistName):
    request = youtubeServiceApi.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": playlistName,
                "description": f"{playlistName} scraped from Spotify.",
                "defaultLanguage": "en",
            },
            "status": {"privacyStatus": "private"},
        },
    )
    try:
        response = request.execute()
    except googleapiclient.errors.HttpError as e:
        print(f"Failed to create playlist on YouTube: {e}")
        raise

    return response
