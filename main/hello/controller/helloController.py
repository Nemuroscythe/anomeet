from flask import (
    Blueprint
)

from main.hello.service import helloService

# Créer un blueprint que l'on doit lié a notre app instance dans __init__
bp = Blueprint('hello', __name__, url_prefix='/')

# Ce fichier contient tout nos points d'entrées (endpoints) pour la partie "hello"

# Une simple page sur /hello HTTP method par défaut : GET
@bp.route('/hello')
def getHello():
    return helloService.getHelloMessage()
