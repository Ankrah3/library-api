from pymongo import MongoClient
from app.config import settings

mongo_client = MongoClient(settings.mongo_url)
mongo_db = mongo_client.get_database()