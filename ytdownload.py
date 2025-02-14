import yt_dlp

url = "Video_Link_Here"  # Replace with your video URL


ydl_opts = {
    'format': 'best',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download complete!")
