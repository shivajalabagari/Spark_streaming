# data_generator.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, rand
import json
import random
import time
from kafka import KafkaProducer
from config.kafka_config import KAFKA_BROKER, KAFKA_TOPIC

spark = SparkSession.builder.appName("DataGenerator").getOrCreate()
producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER, value_serializer=lambda v: json.dumps(v).encode("utf-8"))

def generate_data():
    user_id = random.randint(1, 1000)
    item_id = random.randint(1, 100)
    interaction_type = random.choice(["click", "view", "purchase"])
    timestamp = int(time.time())
    return {"user_id": user_id, "item_id": item_id, "interaction_type": interaction_type, "timestamp": timestamp}

while True:
    data = generate_data()
    producer.send(KAFKA_TOPIC, data)
    print("Produced:", data)
    time.sleep(1)
