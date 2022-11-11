from main import app
from main import database as db
from main.hello.models.HelloMessage import HelloMessage


# Ce fichier sert à la communication avec la base de donnée
def getHelloMessage():
    dbResponse = db.session.execute(db.select(HelloMessage)).first()
    app.logger.info(type(dbResponse))  # Row est une classe de SQLAlchemy qui fonctionne comme un tuple
    return dbResponse[0]
