# flask
from flask import Flask, render_template, request, session, redirect, url_for

import requests
  
#创建flask duixiang
app = Flask(__name__)

app.secret_key = 'BAD_SECRET_KEY'

#返回一些数据给浏览器
@app.route("/Index")
def Index():
  return render_template("Index.html")
 
@app.route("/about")
def about():
  return render_template('about.html')

@app.route("/menu")
def menu(chapter):  
  return render_template('menu.html')

@app.route("/reservation")
def reservation(chapter):  
  return render_template('reservation.html')

@app.route("/shop")
def shop(chapter):  
  return render_template('shop.html')

# Details on the Secret Key: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY
# NOTE: The secret key is used to cryptographically-sign the cookies used for storing
#       the session data.

if __name__ == '__main__':
    app.run()
