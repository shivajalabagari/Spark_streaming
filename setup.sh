# setup.sh
#!/bin/bash
pip install -r requirements.txt
docker-compose up -d
python data_generator.py &
python consumer.py &
cd dashboard && python app.py &
