import yt_dlp

url = 'https://www.instagram.com/reel/DEiWI9vP3mf/?utm_source=ig_web_copy_link'

def my_hook(d):
   lambda d: print(f"Baixando: {d['filename']} - {d['downloaded_bytes']} bytes baixados")

options = {
     'format': 'bestvideo+bestaudio/best',
     'noplaylist': True,
     'outtmpl': 'downloads/%(title)s.%(ext)s',
     # código abaixo extrai áudio de vídeo
     # 'postprocessors': [{
     #    'key': 'FFmpegExtractAudio',
     #    'preferredcodec': 'mp3',
     #    'preferredquality': '192',
     # }],
     'progress_hooks': [my_hook],
}

with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download(url)