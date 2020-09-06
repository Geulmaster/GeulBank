from pymongo import MongoClient

def collection():
    client = MongoClient("mongodb://db:27017")
    db = client.BankAPI
    users = db["users"]
    return users

users = collection()

def user_exists(username):
    if users.find({"Username":username}).count() == 0:
        return False
    else:
        return True