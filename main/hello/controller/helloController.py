from flask import (
    Blueprint, jsonify, request
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


@bp.route('/hello', methods=["POST"])
def createHelloMessage():
    body = request.json  # request permet de récupérer des informations, ici le body s'il est en json
    message = helloService.createHelloMessage(body)
    return jsonify(message.__dict__), 201  # 201 --> HTTP code/status pour "created"


@bp.route('/hello/<id>', methods=["PUT"])
def updateHelloMessage(id):  # Notez comment je passe et récupère une variable dans l'url
    body = request.json
    helloService.updateHelloMessage(id, body)
    return "", 204  # 204 --> HTTP code/status pour "no content" qui signifie que l'appel et réussi mais ne renvoie rien
