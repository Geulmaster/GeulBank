from flask import request, jsonify
from flask_restful import Resource
import bcrypt
from GeulBank.web.helpers import wrapper

users = wrapper.collection()

class Register(Resource):
    def post(self):
        postedData = request.get_json()
        username = postedData["username"]
        password = postedData["password"]
        if wrapper.user_exists(username):
            retJson = {
                'status': 401,
                'msg': 'Invalid Username'
            }
            return jsonify(retJson)
        hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        users.insert({
            "username": username,
            "password": hashed_pw,
            "Own":0,
            "Debt": 0
        })
        retJson = {
            "status": 200,
            "msg": "Successfully signed up for the API"
        }
        return jsonify(retJson)

class Add(Resource):
    def post(self):
        postedData = request.get_json()
        username = postedData["username"]
        password = postedData["password"]
        money = postedData["amount"]
        retJson, error = wrapper.verifyCredentials(username, password)
        if error:
            return jsonify(retJson)
        if money <= 0:
            return jsonify(wrapper.generatedReturnDictionary(404, "The inserted money amount must be greater than 0"))
        cash = wrapper.cashWithUser(username)
        money -= 1 #Transaction fee
        bank_cash = wrapper.cashWithUser("BANK")
        wrapper.updateAccount("BANK", bank_cash + 1)
        wrapper.updateAccount(username, cash + money)
        return jsonify(wrapper.generatedReturnDictionary(200, f"{cash} jubot added successfully to {username}"))