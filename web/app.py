from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt

from GeulBank.web.helpers import wrapper

app = Flask(__name__)
api = Api(app)

users = wrapper.collection()