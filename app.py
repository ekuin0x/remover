from flask import Flask, flash, request, redirect, url_for, render_template
from rembg import remove
from fire import storage
import pyrebase

config = {
  "apiKey": "AIzaSyBFj4WtVAfarJFy0V6YwccqTNplYajofOo",
  "authDomain": "ytconvert-f92e2.firebaseapp.com",
  "databaseURL": "",
  "storageBucket": "ytconvert-f92e2.appspot.com",
  "appId": "1:479741046984:web:5e86d7729e55b5760ab5fd",
  "measurementId": "G-DSWWEJCHDT"
}

app = Flask(__name__)

@app.route("/")
def index() :
    return render_template("index.html")

@app.route('/data', methods = ['POST'])
def data():
    if request.method == 'POST': 
        img = request.files['file']
        name = "(no_background)" + img.filename
        i = remove(img.read())
        storage.child(name).put(i)
        url = storage.child(name).get_url("")
        return url     
    
    return "PROBLEM OCCURED"

if __name__ == '__main__' :
    app.run(debug=True)