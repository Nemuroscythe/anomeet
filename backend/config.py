import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    TESTING = False
    DEVELOPMENT = True
    DEBUG = True
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'

    HOST = os.getenv("HOST")
    USER = os.getenv("USER")
    PASSWORD = os.getenv("PASSWORD")
    DATABASE = os.getenv("DATABASE")
    PORT = os.getenv("PORT")
    PSYCOPG2_CONNECTION_STRING = "host=%s dbname=%s user=%s password=%s port=%s" % (HOST, DATABASE, USER, PASSWORD, PORT)