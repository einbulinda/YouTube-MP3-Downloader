## Table of Contents

- [YouTube Playlist Audio Downloader](#youtube-playlist-audio-downloader)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Example](#example)
  - [Customization](#customization)
    - [Max Workers (Parallel Downloads)](#max-workers-parallel-downloads)
    - [Logs](#logs)
    - [Progress Tracking](#progress-tracking)
  - [Troubleshooting](#troubleshooting)
    - [FFmpeg not found](#ffmpeg-not-found)
    - [yt-dlp Throttling or Timeout Issues](#yt-dlp-throttling-or-timeout-issues)
  - [Contributing](#contributing)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)


# YouTube Playlist Audio Downloader

A Python application that allows you to download entire YouTube playlists as audio files (in MP3 format) 
with multithreaded downloading for improved performance. 
The application supports parallel downloads and automatically skips videos that have already 
been downloaded. 
It also logs any errors or skipped videos into a log file for future reference.


## Features

- **Download entire YouTube playlists** as audio files (MP3 format).
- **Multithreaded downloading**: Download multiple videos in parallel for faster performance.
- **Skip previously downloaded videos** using an archive file (`downloaded_videos.txt`).
- **Error handling and logging**: Automatically skips videos that can't be downloaded and logs them to a `skipped_videos.txt` file.
- **Progress tracking**: Displays download progress by showing how many videos have been downloaded out of the total.

## Prerequisites

Before using the application, make sure you have the following installed:

1. **Python 3.6 or above**: [Download Python](https://www.python.org/downloads/)
2. **yt-dlp**: A YouTube downloader library.
   Install via pip:
   ```bash
   pip install yt-dlp

3. **FFmpeg**: Required for audio extraction and conversion. 
- Download and install FFmpeg from the [official site](https://ffmpeg.org/download.html) and ensure it is added to your system's PATH.

## Installation
1. Clone the repository or download the script:

    ```bash
    git clone https://github.com/einbulinda/YouTube-MP3-Downloader.git
    cd YouTube-MP3-Downloader

2. Install the required Python libraries:

    ```bash    
    pip install -r requirements.txt
   ```

   **Note**: If `requirements.txt` is not provided, simply run:

   ```bash   
   pip install yt-dlp

## Usage
1. Run the Python script:

   ```bash   
   python download_playlist_audio.py

2. When prompted, enter the following:
    - **YouTube Playlist URL**: Enter the URL of the YouTube playlist you want to download.
    - **Save Path**: Enter the folder path where the audio files should be saved (e.g., `C:/Users/YourName/Music`).

3. The application will then:
    - Download all videos in the playlist as audio files (MP3 format).
    - Show download progress (number of videos downloaded out of the total).
    - Skip any videos that have already been downloaded.
    - Log any errors to a `skipped_videos.txt` file.

## Example

```bash
python download_playlist_audio.py
Enter YouTube playlist URL: https://www.youtube.com/playlist?list=PLx6y3f7fuEkxzDg7X5Kdfg
Enter the folder path to save audio: C:/Users/YourName/Music

Starting download of 10 videos in parallel...
Downloaded and converted: https://www.youtube.com/watch?v=xyz123
Progress: 1/10 videos downloaded.
Downloaded and converted: https://www.youtube.com/watch?v=abc456
Progress: 2/10 videos downloaded.
Error downloading https://www.youtube.com/watch?v=error_vid: 404 Not Found
Progress: 3/10 videos downloaded.
...
Playlist audio download completed!

```

## Customization
### Max Workers (Parallel Downloads)

You can adjust the number of videos being downloaded concurrently by changing the `max_workers` parameter:

```python

download_playlist_as_audio_parallel(playlist_url, save_path, max_workers=4)

```

Increasing `max_workers` will download more videos at the same time, but be cautious as this may consume more network bandwidth.

### Logs

The application automatically logs any videos that couldn't be downloaded into a `skipped_videos.txt` file. This file will contain the video URL and the error message.


### Progress Tracking
The progress of the download is displayed after each video is processed, showing how many videos have been downloaded out of the total number.

## Troubleshooting

### FFmpeg not found
If you encounter errors related to FFmpeg, ensure that FFmpeg is installed and added to your system's PATH. You can verify this by running:

```bash
ffmpeg -version
```

If the command is not recognized, reinstall FFmpeg and ensure the installation directory is added to your system's PATH.

### yt-dlp Throttling or Timeout Issues

If you encounter issues such as `HTTPSConnectionPool` or timeout errors, you can try increasing the timeout in the code by modifying the `socket_timeout` option:

```python
'socket_timeout': 120,  # Increase to 120 seconds
```

### Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for making video/audio downloads from YouTube easier.
- [FFmpeg](https://ffmpeg.org/) for handling audio conversion.

