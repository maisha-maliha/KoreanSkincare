import pymongo
from pymongo import MongoClient
import pymongo.errors
from models.config import MONGO_URI


def mongodb_database_connection(func):
    def wrapper(*args, **kwargs):
        try:
            client = MongoClient(MONGO_URI)
            database = client.get_database("KoreanSkinCare")
            collection = database["productDetails"]
            return func(*args, **kwargs, collection=collection)
        except pymongo.errors.ConnectionFailure as err:
            print("mongodb database connection error:", err)
        finally:
            client.close()
        return None

    return wrapper
