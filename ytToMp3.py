import pytube
from moviepy.editor import *


def convert_to_mp3():
    mp4_file = 'download.mp4'
    videoclip = VideoFileClip(mp4_file)
    audioclip = videoclip.audio
    audioclip.write_audiofile('download.mp3')
    audioclip.close()
    videoclip.close()


def download_video(url):
    youtube = pytube.YouTube(url)
    video = youtube.streams.first()
    video.download(filename='download')
    convert_to_mp3()


def main():
    url = input("enter url: ")
    download_video(url)


if __name__ == "__main__":
    main()
