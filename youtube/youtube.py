from __future__ import unicode_literals
import youtube_dl
import os
url='https://www.youtube.com/watch?v=aRnKqRqxHRM'

ydl_opts = {
'format':'bestvideo[height<=240]',
'getdescription':'True'}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	#info = ydl.extract_info(url, download=False)
	ydl.download([url])

#os.system('python upload.py --file="" --title="title1" --description="description1" --keywords="keywords" --category="22" --privacyStatus="private"')
