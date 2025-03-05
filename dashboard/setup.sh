#!/bin/bash
echo "Installing dependencies..."
pip install -r requirements.txt

echo "Starting Docker services..."
docker-compose up -d

echo "Starting data generator..."
python data_generator.py &

echo "Starting Kafka consumer..."
python consumer.py &

echo "Starting Flask dashboard..."
cd dashboard && python app.py &
