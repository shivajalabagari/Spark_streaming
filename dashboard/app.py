# dashboard/app.py
from flask import Flask, render_template
from pymongo import MongoClient
from config.db_config import MONGO_URI, MONGO_DB, MONGO_COLLECTION

app = Flask(__name__)
client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

@app.route("/")
def index():
    interactions = list(collection.find().limit(100))
    return render_template("index.html", interactions=interactions)

if __name__ == "__main__":
    app.run(debug=True)
