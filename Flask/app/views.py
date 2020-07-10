from flask_pymongo import PyMongo
from app import server

mongoConn = PyMongo(server)

Users = mongoConn.db.users

st_shp = mongoConn.db.st_shp