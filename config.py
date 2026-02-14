import os

class Config:

    GEMINI_API_KEY = "AIzaSyAh6npPN3JE-4tunQc3M2hiHfvKM_4EV74"
    DATABASE_URL = "sqlite:///database.db"
    SECRET_KEY = "mysecret12345678"
    DEBUG = os.getenv("FLASK_DEBUG", "True") == "True"


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
