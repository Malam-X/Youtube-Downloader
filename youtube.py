# MODULES

import os,sys
from pytube import YouTube

# Label

print('Youtube Downloader')

x = input('[+] Enter Url: ')
if x == '':
	print('[+] Try Again...')
else:
	if sys.platform.startswith('linux'):
		os.system('clear')
	else:
		os.system('cls')
	print('Loading')
	done = YouTube(x)

print('''
	[+] Title    : {}
	[+] Thumbnail: {}
    '''.format(done.title, done.thumbnail_url))

try:
	print('\n\n[+] Video Downloaded.')
	for s in done.streams:
		print(x)
	done = done.s.get_highest_resolution()
	done.download()
except:
	print('[!] Unsuccessfully...')
