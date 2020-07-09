import os

class Config(object):
      SECRET_KEY = os.environ.get('SECRET_KEY') or '8a3f733cbf323ad0c521904374783741'
      MONGO_URI = os.environ.get('MONGO_URI')