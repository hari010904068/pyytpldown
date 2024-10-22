import yt_dlp
import os

def download_playlist(playlist_url, download_path):
    # Ensure the download directory exists
    if not os.path.exists(download_path):
        os.makedirs(download_path)
#test1
    # Set up yt-dlp options
    ydl_opts = {
        'format': 'bestvideo[ext=mp4][height<=1440]+bestaudio[ext=m4a]/best[ext=mp4]',  # Download best MP4 video up to 1440p and best audio
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # Define output file naming format
        'merge_output_format': 'mp4',  # Ensure both audio and video are merged in MP4 format
        'noplaylist': False,  # Ensure it downloads the entire playlist
    }

    # Download the playlist
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

# Example usage
playlist_url = input("Enter the playlist URL: ")
download_path = "youtube_playlist_downloads"  # Define the download directory

download_playlist(playlist_url, download_path)
