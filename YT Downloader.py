from pytube import YouTube
from sys import argv


yt = YouTube(argv[1])
video = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
video.download('/Users/alex/Documents/Downloads/')
print('Success!')