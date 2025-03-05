# data_generator.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, rand
import json
import random
import time
from kafka import KafkaProducer
from config.kafka_config import KAFKA_BROKER, KAFKA_TOPIC
