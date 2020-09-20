from io import *
import os
from flask import Flask, redirect, url_for, request, send_from_directory
from werkzeug.utils import secure_filename
import time


app = Flask(__name__)

@app.route('/success/')
def success(name):
	#print("__________ recieved : "+str(name))
	return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['data']
      saveLogs(user)
      return 'welcome %s' % user
      #return redirect(url_for('success',name = user))
   else:
      user = request.args.get('data')
      saveLogs(user)
      return 'welcome %s' % user
      #return redirect(url_for('success',name = user))

@app.route("/upload", methods=['POST'])
def upload_file():
   if request.method == 'POST':

      file = request.files['ScreenShoot']
      if file and allowed_file(file.filename):
         filename = str(time.time())+"_"+secure_filename(file.filename)
         path = os.path.join('UPLOAD_FOLDER', filename)
         file.save(path)
         #send_from_directory('UPLOAD_FOLDER',filename)
         info = file.filename+" ["+str(get_size_format(os.stat(path).st_size))+"] UPLOADED SUCCESSFULLY!"

      return info


def saveLogs(l):
	with open('logs.txt', 'w') as file:
		file.write(l)



def allowed_file(filename):
   return filename[-3:].lower() in set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4'])

def get_size_format(b, factor=1024, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"


if __name__ == '__main__':
   app.run(debug = True)