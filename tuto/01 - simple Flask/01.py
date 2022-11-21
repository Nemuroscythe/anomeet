# import de Flask:
from flask import Flask


# Initialisation de l'objet
# ! pour alwaysdata il faut que cet objet soit
# nommé 'application'
application = Flask(__name__)


# Définition de la route par défaut
# en utilisant un décorateur de fonction
# c'est le '@', manière la plus facile
@application.route("/")
def index():
	return "Hello Anomeet!"

# Je n'ai pas spécifié de méthodes ici,
# car par défaut elle vaut 'GET'
# et c'est la méthodes par défaut également
# d'un navigateur.


# On lance le serveur en appelant la fonction
# interne de l'objet flask : run
application.run()


# Lancer un navigateur web et aller sur
# localhost:5000