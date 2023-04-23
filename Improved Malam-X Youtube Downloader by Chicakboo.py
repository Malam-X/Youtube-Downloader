# MODULES
import os
import sys
from pytube import YouTube

# Clear Screen
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# LABEL
print('Youtube Downloader')

# USER INPUT
url = input('[+] Enter URL: ')
if url == '':
    print('[+] Try Again...')
    sys.exit()
else:
    clear()
    print('Loading')
    video = YouTube(url)

# VIDEO INFORMATION
print(f'[+] Title    : {video.title}')
print(f'[+] Thumbnail: {video.thumbnail_url}')

# VIDEO OR AUDIO DOWNLOAD
while True:
    choice = input('[+] Do you want to download (V)ideo or (A)udio? ').lower()
    if choice == 'v':
        stream = video.streams.get_highest_resolution()
        stream.download()
        print('[+] Video Downloaded.')
        break
    elif choice == 'a':
        stream = video.streams.filter(only_audio=True).first()
        stream.download()
        print('[+] Audio Downloaded.')
        break
    else:
        print('[!] Invalid Choice. Please enter V or A.')

