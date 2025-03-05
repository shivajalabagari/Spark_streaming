from pyspark.sql import SparkSession
from kafka import KafkaConsumer
from pymongo import MongoClient
import json

consumer = KafkaConsumer("user_interactions", bootstrap_servers="localhost:9092", value_deserializer=lambda x: json.loads(x.decode("utf-8")))
client = MongoClient("mongodb://localhost:27017")
db = client["analytics"]
collection = db["interactions"]

for message in consumer:
    data = message.value
    collection.insert_one(data)
    print("Stored:", data)
