from flask import Flask, jsonify, render_template, redirect, request 
import os
from secrets import token_urlsafe
import redis

app = Flask(__name__)
db = redis.Redis(host = os.getenv("REDISHOST"), port=os.getenv("REDISPORT"), password=os.getenv("REDISPASSWORD"))

@app.route('/') 
def index(): 
    return render_template("form.html") 

@app.route("/link", methods = ['POST'])
def link():
    if request.form.get("password") != os.getenv("PASSWORD"):
        return render_template("<h1> wrong password </h1>"), 401
    db.set(request.form.get("key"), request.form.get("value"))
    return render_template("<h1> done </h1>")

@app.route("/<slug>")
def return_link(slug):
    if not db.exists(slug):
        return "url doesn't exist"
    return redirect(db.get(slug))

@app.route('/shorten')
def shorten():
    pass

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
