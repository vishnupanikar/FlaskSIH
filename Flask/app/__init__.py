from flask import Flask
from config import Config

server = Flask(__name__)
server.config.from_object(Config)


from app import routes