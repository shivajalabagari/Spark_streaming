# data_generator.py
from pyspark.sql import SparkSession
import json
import random
import time
from kafka import KafkaProducer
from config.kafka_config import KAFKA_BROKER, KAFKA_TOPIC

producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER, value_serializer=lambda v: json.dumps(v).encode("utf-8"))

def generate_data():
    return {
        "user_id": random.randint(1, 1000),
        "item_id": random.randint(1, 100),
        "interaction_type": random.choice(["click", "view", "purchase"]),
        "timestamp": int(time.time())
    }

while True:
    data = generate_data()
    producer.send(KAFKA_TOPIC, data)
    print("Produced:", data)
    time.sleep(1)

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