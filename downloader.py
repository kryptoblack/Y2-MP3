import youtube_dl
import sys
import logging

logging.basicConfig(filename='app.log', filemode='a',
                    format='%(message)s', level=20)

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'out/%(extractor_key)s/%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'noplaylist': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': logging.getLogger(),
}


if __name__ == "__main__":
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        filenames = sys.argv[1:]
        ydl.download(filenames)
