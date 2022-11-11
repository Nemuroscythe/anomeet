# Configuration / variables d'environnements pour le développement local
DEVELOPMENT = True
DEBUG = True
CSRF_ENABLED = True
SECRET_KEY = 'this-really-needs-to-be-changed'

BASE_URL = 'localhost'
DATABASE_PORT = '5432'
USERNAME = 'test-anomeet_application'
PASSWORD = 'Application_Anomeet'
DATABASE = 'test-anomeet_Postgresql'
SQLALCHEMY_DATABASE_URI = f"postgresql://{USERNAME}:{PASSWORD}@{BASE_URL}:{DATABASE_PORT}/{DATABASE}"
