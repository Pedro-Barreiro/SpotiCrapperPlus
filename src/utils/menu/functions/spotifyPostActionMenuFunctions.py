import utils.youtube.index as youtube


def choice1Playlist(playlist):
    print("Importing to Youtube playlist...")
    # Get playlists from YouTube
    try:
        youtubeServiceApi = youtube.getYoutubeOauth()
        youtubePlaylists = youtube.listYoutubePlaylists(
            youtubeServiceApi, playlist["playlist_name"]
        )
    except Exception as e:
        print(f"Failed to check playlist on YouTube: {e}")
        return

    # Check if playlist already exists on YouTube
    ytPlaylistId = None
    for ytPlaylist in youtubePlaylists["items"]:
        if ytPlaylist["snippet"]["title"] == playlist["playlist_name"]:
            ytPlaylistId = ytPlaylist["id"]
            print("Playlist already exists on YouTube")
            break

    # Search for each track on YouTube
    youtubeVideoIds = []
    for track in playlist["tracks"]:
        try:
            youtubeVideo = youtube.searchYoutubeVideo(
                youtubeServiceApi, track["name"], track["artist"]
            )
            youtubeVideoId = youtubeVideo["items"][0]["id"]["videoId"]
            youtubeVideoIds.append(youtubeVideoId)
            print(f"Found video on YouTube: {youtubeVideoId}")
        except Exception as e:
            print(f"Failed to search video on YouTube: {e}")
            continue

    # If playlist does not exist on YouTube, create it
    if ytPlaylistId is None:
        try:
            youtubePlaylist = youtube.createYoutubePlaylist(
                youtubeServiceApi, playlist["playlist_name"]
            )
            ytPlaylistId = youtubePlaylist["id"]
            print("Created playlist on YouTube")
        except Exception as e:
            print(f"Failed to create playlist on YouTube: {e}")
    else:
        # If playlist exists on YouTube, list all videos
        youtubePlaylistVideosIds = []
        try:
            youtubePlaylistVideos = youtube.listVideosFromYoutubePlaylist(
                youtubeServiceApi, ytPlaylistId
            )
            for youtubePlaylistVideo in youtubePlaylistVideos["items"]:
                youtubePlaylistVideosIds.append(
                    youtubePlaylistVideo["contentDetails"]["videoId"]
                )
        except Exception as e:
            print(f"Failed to list videos from YouTube playlist: {e}")
            return

    # Check if video already exists on YouTube playlist
    youtubeVideoIds = list(set(youtubeVideoIds) - set(youtubePlaylistVideosIds))

    # Add videos to YouTube playlist
    for youtubeVideoId in youtubeVideoIds:
        try:
            youtube.addVideoToYoutubePlaylist(
                youtubeServiceApi, ytPlaylistId, youtubeVideoId
            )
            print("Added video to playlist on YouTube")
        except Exception as e:
            print(f"Failed to add video to playlist on YouTube: {e}")


def choice1Album(album):
    # TODO: Search for album on youtube and add to channel
    print(f"---\nAlbum: {album['album_name']}")
    print(f"Artist: {album['artist_name']}")
    print("Tracks:")
    for track in album["tracks"]:
        print(f"- {track}")


def choice2Playlist(playlist):
    print("Creating JSON file...")
    import json

    with open(f"{playlist['playlist_name']}.json", "w") as f:
        json.dump(playlist, f)
    print("Created JSON file")


def choice2Album(album):
    print("Creating JSON file...")
    import json

    with open(f"{album['album_name']}.json", "w") as f:
        json.dump(album, f)
    print("Created JSON file")
