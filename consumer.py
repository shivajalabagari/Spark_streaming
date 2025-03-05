# consumer.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, avg
from kafka import KafkaConsumer
from pymongo import MongoClient
from config.kafka_config import KAFKA_BROKER, KAFKA_TOPIC
from config.db_config import MONGO_URI, MONGO_DB, MONGO_COLLECTION
import json

spark = SparkSession.builder.appName("KafkaConsumer").getOrCreate()
client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_BROKER, value_deserializer=lambda x: json.loads(x.decode("utf-8")))
data = []
for message in consumer:
    data.append(message.value)
    if len(data) >= 10:
        df = spark.createDataFrame(data)
        aggregated_df = df.groupBy("user_id").agg(count("interaction_type").alias("interaction_count"), avg("item_id").alias("avg_item"))
        result = aggregated_df.toPandas().to_dict("records")
        collection.insert_many(result)
        print("Stored Aggregated Data:", result)
        data = []
