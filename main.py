from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route("/d")
def d():
    return render_template("<h1> a </h1>")

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
