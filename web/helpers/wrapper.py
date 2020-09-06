from pymongo import MongoClient
import bcrypt

def collection():
    client = MongoClient("mongodb://localhost:27017") #geulbank_db_1 instead localhost
    db = client["BankAPI"]
    users = db["users"]
    return users

users = collection()

def user_exists(username):
    if users.find({"Username":username}).count() == 0:
        return False
    else:
        return True

def verifyPW(username, password):
    if not user_exists(username):
        return False
    hashed_pw = users.find({
        "Username":username
    })[0]["Password"]
    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    else:
        return False

def cashWithUser(username):
    cash = users.find({
        "Username":username
    })[0]["Own"]
    return cash

def debtWithUser(username):
    debt = users.find({
        "Username":username
    })[0]["Debt"]
    return debt

def generatedReturnDictionary(status, msg):
    retJson = {
        "status": status,
        "msg": msg
    }
    return retJson

def verifyCredentials(username, password):
    if not user_exists(username):
        return generatedReturnDictionary(401, "Invalid Username"), True
    correct_pw = verifyPW(username, password)
    if not correct_pw:
        return generatedReturnDictionary(402, "Incorrect Password"), True
    return None, False

def updateAccount(username, balance):
    users.update({
        "Username": username
    },{
        "$set":{
            "Own": balance
        }
    })

def updateDebt(username, balance):
    users.update({
        "Username": username
    },{
        "$set":{
            "Debt": balance
        }
    })
