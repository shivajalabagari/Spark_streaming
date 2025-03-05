# dashboard/dashboard.py
from pymongo import MongoClient
from config.db_config import MONGO_URI, MONGO_DB, MONGO_COLLECTION

def get_aggregated_data():
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DB]
    collection = db[MONGO_COLLECTION]
    pipeline = [
        {"$group": {"_id": "$user_id", "interaction_count": {"$sum": 1}}},
        {"$sort": {"interaction_count": -1}}
    ]
    return list(collection.aggregate(pipeline))