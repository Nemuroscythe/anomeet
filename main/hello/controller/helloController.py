from flask import (
    Blueprint,jsonify
)

from main.hello.service import helloService

# Ce fichier contient tout nos points d'entrées (endpoints) pour la partie "hello"

# Créer un blueprint qu'on doit lié a notre app instance dans __init__
bp = Blueprint('hello', __name__, url_prefix='/')


# Une simple page sur /hello HTTP method par défaut : GET
@bp.route('/hello')
def getHello():
    message = helloService.getHelloMessage()
    return jsonify(message.__dict__)
