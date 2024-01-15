from dotenv import load_dotenv
import os
import googleapiclient.discovery
import google_auth_oauthlib.flow

load_dotenv()

scopes = ['https://www.googleapis.com/auth/youtube.force-ssl']

# Add tracks to YouTube playlist
def createYTPlaylist(playlistName):
    # Disable OAuthlib's HTTPS verification when running locally.
    # !!DO NOT leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = os.getenv('YT_CLIENT_SECRETS_FILE')


    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes
    )

    credentials = flow.run_local_server(port=0)

    youtube = googleapiclient.discovery.build(
        api_service_name,
        api_version,
        credentials=credentials
    )

    request = youtube.playlists().insert(
        part="snippet,status",
        body={
          "snippet": {
            "title": playlistName,
            "description": f"{playlistName} scraped from Spotify.",
            "defaultLanguage": "en"
          },
          "status": {
            "privacyStatus": "private"
          }
        }
    )
    response = request.execute()

    print(response)