from flask import Flask,render_template,request,jsonify,redirect,url_for
from downloader import download
import unicodedata
import os
app = Flask(__name__)

@app.route("/download",methods=['GET'])
def download_func():
	url='https://www.youtube.com/watch?v=aRnKqRqxHRM'
	options={}
	options['format']='bestvideo[height<=480]+bestaudio/best[height<=480]'
	options['outtmpl']='%(title)s.%(ext)s'
	info=download(url,options)
	os.system('python upload.py --file="'+info['title']+'.'+info['ext']+'" --title="'+info['title']+'" --description="'+info['description']+'" --keywords="keywords" --category="22" --privacyStatus="private"')
	return jsonify(info)



'''
@app.route("/download",methods=['GET'])
def download_func():
	url='https://www.youtube.com/watch?v=aRnKqRqxHRM'
	options={}
	options['format']='bestvideo[height<=480]+bestaudio/best[height<=480]'
	info=download(url,options)
	return redirect(url_for('upload',ext=info['ext'],title=info['title'],description=info['description']))

@app.route("/upload/<ext>/<title>/<description>")
def upload(ext,title,description):
	os.system('python upload.py --file='+ext+' --title='+title+' --description='+description+' --keywords="keywords" --category="22" --privacyStatus="private"')
	return "uploaded"

'''
if __name__ == "__main__":
    app.run(debug=True)
