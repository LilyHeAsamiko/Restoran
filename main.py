# flask

from flask import Flask, render_template, request, session, redirect, url_for

import requests
  
#创建flask duixiang
app = Flask(__name__)

app.secret_key = 'BAD_SECRET_KEY'

#返回一些数据给浏览器
@app.route("/index")
def index():
  return render_template("index.html")
 
@app.route("/book")
def book():
  return render_template('book.html')

@app.route("/contact")
def danci(chapter):  
  return render_template('contact.html')

# Details on the Secret Key: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY
# NOTE: The secret key is used to cryptographically-sign the cookies used for storing
#       the session data.

if __name__ == '__main__':
    app.run()
