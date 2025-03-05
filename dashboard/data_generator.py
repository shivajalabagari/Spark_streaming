from pyspark.sql import SparkSession
import json
import random
import time
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers="localhost:9092", value_serializer=lambda v: json.dumps(v).encode("utf-8"))

def generate_data():
    return {"user_id": random.randint(1, 1000), "item_id": random.randint(1, 100), "interaction_type": random.choice(["click", "view", "purchase"]), "timestamp": int(time.time())}

while True:
    data = generate_data()
    producer.send("user_interactions", data)
    print("Produced:", data)
    time.sleep(1)
