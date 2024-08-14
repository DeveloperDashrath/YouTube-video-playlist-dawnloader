import yt_dlp
import ffmpeg

def download_playlist(playlist_url, download_path='.', quality='best'):
    ydl_opts = {
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',  # Output template
        'format': f'bestvideo[height<={quality}]+bestaudio/best' if quality != 'best' else 'best',  # Avoids merging by selecting combined streams
        'merge_output_format': 'mp4',  # Specify output format
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Convert to mp4 if needed
        }] if quality == 'best' else [],  # Only add this if using best quality
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

if __name__ == "__main__":
    playlist_url = input("Enter the playlist URL: ")
    download_path = input("Enter the download path (default is current directory): ") or '/storage/emulated/0/Download/Python ki khodiya'
    
    print("Choose video quality:")
    print("1. best (default)")
    print("2. worst")
    print("3. 1080p")
    print("4. 720p")
    print("5. 480p")
    print("6. 360p")
    
    quality_choice = input("Enter the number corresponding to your choice: ")

    quality_map = {
        '1': 'best',
        '2': 'worst',
        '3': '1080',
        '4': '720',
        '5': '480',
        '6': '360'
    }

    quality = quality_map.get(quality_choice, 'best')  # Default to 'best' if invalid choice

    download_playlist(playlist_url, download_path, quality)
