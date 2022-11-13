from main import app
from main import database as db
from main.hello.models.HelloMessage import HelloMessage


# Ce fichier sert à la communication avec la base de données
def getHelloMessage():
    dbResponse = db.session.execute(db.select(HelloMessage)).first()
    app.logger.info(type(dbResponse))  # Row est une classe de SQLAlchemy qui fonctionne comme un tuple
    return dbResponse[0]


def createHelloMessage(helloMessage):
    db.session.add(helloMessage)
    db.session.commit()
    return None


def updateHelloMessage(helloMessage):
    app.logger.debug(helloMessage)
    helloMessageDB = db.get_or_404(HelloMessage, helloMessage.id) # Je récupère la donnée liée à l'id, nécessaire pour l'ORM
    helloMessageDB.content = helloMessage.content # J'effectue une mise à jour de la donnée, ce qui est repéré par l'ORM
    db.session.commit() #Je commit se changement dans la bdd
    return None


def deleteHelloMessage(id):
    helloMessageDB = db.get_or_404(HelloMessage, id) # Je récupère la donnée liée à l'id, nécessaire pour l'ORM
    db.session.delete(helloMessageDB)
    db.session.commit() #Je commit se changement dans la bdd
    return None