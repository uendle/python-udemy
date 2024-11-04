from  pytubefix import *

youtube = YouTube(input('Digite a url: '))

print(youtube.title)
print(youtube.thumbnail_url)

stream = youtube.streams.get_highest_resolution()

stream.download()
