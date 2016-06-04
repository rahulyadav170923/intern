from __future__ import unicode_literals
import youtube_dl
import os

def download(url,ydl_opts):
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		info = ydl.extract_info(url, download=False)
		ydl.download([url])
	needed_info={}
	needed_info['title']=info['title']
	needed_info['description']=info['description']
	needed_info['categories']=info['categories']
	needed_info['ext']=info['ext']
	return needed_info

#os.system('python upload.py --file="" --title="title1" --description="description1" --keywords="keywords" --category="22" --privacyStatus="private"')
