from flask import Flask, jsonify, render_template, redirect 
import os
from secrets import token_urlsafe
import redis

app = Flask(__name__)
db = redis.Redis(host = os.getenv("REDISHOST"), port=os.getenv("REDISPORT"), password=os.getenv("REDISPASSWORD"))

@app.route('/') 
def index(): 
    return render_template("form.html") 

@app.route("/link", methods = ['POST'])
def link(request):
   print(request.form) 

@app.route("/<slug>")
def return_link(slug):
    pass

@app.route('/shorten')
def shorten():
    pass

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
