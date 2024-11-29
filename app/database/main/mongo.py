from typing import Collection
from pymongo import MongoClient
from app.config import settings


MONGO_URI = settings.MONGODB_URL
DATABASE_NAME = settings.MONGODB_DB

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]

users_collection = db["users"]
notes_collection = db["notes"]

def get_db():
    connection_string = MONGO_URI
    client = MongoClient(connection_string)
    return client[DATABASE_NAME]

def get_global_collection(collection_name) -> Collection:
    db = get_db()
    if collection_name not in db.list_collection_names():
        db.create_collection(collection_name)
    return db[collection_name]

async def insert_one(collection, document):
    return await collection.insert_one(document)

async def find_one(collection, query):
    return await collection.find_one(query)