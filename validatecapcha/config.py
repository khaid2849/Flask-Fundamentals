import uuid
from pymongo import MongoClient

mongoClient = MongoClient("localhost", 27017)


class Config:
    SECRET_KEY = str(uuid.uuid4())
    CAPTCHA_ENABLE = True
    CAPTCHA_LENGTH = 5
    CAPTCHA_WIDTH = 160
    CAPTCHA_HEIGHT = 60
    SESSION_MONGODB = mongoClient
    SESSION_TYPE = "mongodb"
