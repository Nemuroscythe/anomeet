
class Config:
    TESTING = False
    DEVELOPMENT = True
    DEBUG = True
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'

    HOST = "postgresql-test-anomeet.alwaysdata.net"
    USER = "test-anomeet_application"
    PASSWORD = "Application_Anomeet"
    DATABASE = "test-anomeet_postgresql"
    PORT ="5432"
    PSYCOPG2_CONNECTION_STRING = "host=%s dbname=%s user=%s password=%s port=%s" % (HOST, DATABASE, USER, PASSWORD, PORT)