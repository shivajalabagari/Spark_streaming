# consumer.py
from pyspark.sql import SparkSession
from kafka import KafkaConsumer
from pymongo import MongoClient
import json
from config.kafka_config import KAFKA_BROKER, KAFKA_TOPIC
from config.db_config import MONGO_URI, MONGO_DB, MONGO_COLLECTION

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_BROKER, value_deserializer=lambda x: json.loads(x.decode("utf-8")))

for message in consumer:
    data = message.value
    collection.insert_one(data)
    print("Stored:", data)