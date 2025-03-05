from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017")
db = client["analytics"]
collection = db["interactions"]

@app.route("/")
def index():
    interactions = list(collection.find().limit(100))
    return render_template("index.html", interactions=interactions)

if __name__ == "__main__":
    app.run(debug=True)
