from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt

#delete unused imports

from GeulBank.web.helpers import wrapper
from GeulBank.web.actions import resources

app = Flask(__name__)
api = Api(app)

users = wrapper.collection()

api.add_resource(resources.Register, '/register')