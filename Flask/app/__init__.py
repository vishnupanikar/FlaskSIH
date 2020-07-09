from flask import Flask
from config import Config
from flask_pymongo import PyMongo

server = Flask(__name__)
server.config.from_object(Config)
mongoConn = PyMongo(server)

from app import routes