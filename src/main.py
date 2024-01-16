from dotenv import load_dotenv
from src.utils import spotify_scrapper, youtube

load_dotenv()

def main():
    playlist_id = '37i9dQZF1DX0rV7skaITBo'
    playlist = spotify_scrapper.scrape_playlist(playlist_id)
    print("scraped playlist from Spotify")

    try:
        youtube.createYTPlaylist(playlist['playlist_name'])
        print("created playlist on YouTube")
    except Exception as e:
        print(f"Failed to create playlist on YouTube: {e}")

main()