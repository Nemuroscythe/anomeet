from flask import (
    Blueprint
)
# Créer un blueprint que l'on doit lié a notre app instance dans __init__
bp = Blueprint('hello', __name__, url_prefix='/')

# Une simple page sur /hello HTTP method par défaut : GET
@bp.route('/hello')
def hello():
    return 'Hello, World!'
