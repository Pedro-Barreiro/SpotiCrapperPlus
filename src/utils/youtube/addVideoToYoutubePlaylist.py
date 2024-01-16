import googleapiclient.discovery

def addVideoToYoutubePlaylist(youtubeServiceApi, playlistId, videoId):

    request = youtubeServiceApi.playlistItems().insert(
        part="snippet",
        body={
          "snippet": {
            "playlistId": playlistId,
            "position": 0,
            "resourceId": {
              "kind": "youtube#video",
              "videoId": videoId
            }
          }
        }
    )
    try:
        response = request.execute()
    except googleapiclient.errors.HttpError as e:
        print(f"Failed to insert video to YouTube playlist: {e}")
        raise

    return response