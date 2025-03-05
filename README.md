# README.md
# Data Engineering Hiring Case Study

## Overview
This project demonstrates a real-time data pipeline using Kafka, PySpark, MongoDB, and Flask. It consists of:
1. A data generator that streams user interaction logs to Kafka.
2. A Kafka consumer that processes and aggregates data using PySpark before storing it in MongoDB.
3. A Flask-based dashboard to visualize real-time interaction analytics.

## Technologies Used
- Apache Kafka
- PySpark
- MongoDB
- Flask
- Docker
- Gitpod/GitHub

## Setup Instructions
1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd <repository_directory>
   ```
2. Start the services using Docker:
   ```sh
   docker-compose up -d
   ```
3. Run the data generator:
   ```sh
   python data_generator.py
   ```
4. Start the Kafka consumer:
   ```sh
   python consumer.py
   ```
5. Run the dashboard:
   ```sh
   cd dashboard
   python app.py
   ```
6. Open the dashboard at:
   ```
   http://localhost:5000
   ```

## Expected Output
- The data generator continuously sends user interaction data to Kafka.
- The consumer processes, aggregates, and stores the data in MongoDB.
- The dashboard visualizes the aggregated metrics in real-time.

## Future Enhancements
- Implement alerting for threshold breaches.
- Use a more advanced visualization tool like Grafana.
- Optimize the Kafka consumer for high-throughput scenarios.

## License
This project is open-source and free to use.
