from pymongo import MongoClient
from app.config import MONGO_URI, DB_NAME


client = MongoClient(MONGO_URI)

db = client[DB_NAME]
collection = db.user_learning_profiles
order_collection = db.user_orders
user_style_collection = db.user_style
