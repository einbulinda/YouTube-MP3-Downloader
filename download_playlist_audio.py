import yt_dlp
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
from threading import Lock

# Global variables for progress tracking
progress_lock = Lock()
downloaded_count = 0


# Function to download a video as audio
def download_audio(video_url, save_path, skipped_log_path, total_videos):
    global downloaded_count

    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'ffmpeg_location': r'C:\ffmpeg\bin',
            'socket_timeout': 60,
            'retries': 3,
            'download_archive': 'downloaded_videos.txt',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"Downloaded and converted: {video_url}")
    except Exception as e:
        print(f"Error downloading {video_url}: {str(e)}")
        # Log the skipped video
        with open(skipped_log_path, 'a') as log_file:
            log_file.write(f"{video_url}: {str(e)}\n")
    finally:
        # Update and display the progress
        with progress_lock:
            downloaded_count += 1
            print(f"Progress: {downloaded_count}/{total_videos} videos downloaded.")


# Function to download playlist as audio
def download_playlist_as_audio(playlist_url, save_path, max_workers=4):
    skipped_log_path = os.path.join(save_path, 'skipped_videos.txt')

    try:
        ydl_opts = {
            'extract_flat': 'in_playlist',  # Extract video URLs from playlist without downloading
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            playlist_info = ydl.extract_info(playlist_url, download=False)
            video_urls = [entry['url'] for entry in playlist_info['entries']]

        total_videos = len(video_urls)  # Track total number of videos
        print(f"Downloading {total_videos} videos in parallel...")

        # Use ThreadPoolExecutor to download videos in parallel
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(download_audio, video_url, save_path, skipped_log_path, total_videos) for video_url in video_urls]

            for future in as_completed(futures):
                try:
                    future.result()  # Get the result of the thread (raise exceptions if any)
                except Exception as e:
                    print(f"Error in thread: {str(e)}")

        print("Playlist audio download completed!")
    except Exception as e:
        print(f"Error downloading playlist: {str(e)}")


if __name__ == "__main__":
    # Provide the playlist URL
    playlist_url = input("Enter YouTube playlist URL: ")

    # Directory to save the downloaded audio files
    save_path = input("Enter the folder path to save audio: ")

    download_playlist_as_audio(playlist_url, save_path, max_workers=4)
