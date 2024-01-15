from utils.spotify_scrapper import scrape_playlist
from utils.youtube import createYTPlaylist


def main():
    playlist_id = '37i9dQZF1DX0rV7skaITBo'
    playlist = scrape_playlist(playlist_id)
    print("scraped playlist from Spotify")

    createYTPlaylist(playlist['playlist_name'])
    print("created playlist on YouTube")

main()