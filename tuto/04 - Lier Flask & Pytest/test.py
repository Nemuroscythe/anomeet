import pytest
from flask import Flask

app = Flask(__name__)

# Décorateur Flask et la fonction Python associée.
@app.route("/")
def index():
	return "Hello world"




# Fonction appelée par Pytest pour les tests automatisés.
# Attention que le nom de la fonction doit obligatoirement
# commencer par "test_"
def test_index():
	# Objet de flask permettant de créer un client virtuel
	client = app.test_client()

	# La réponse est le return de ma fonction Flask
	# Ici on fait un GET sur la route "/"
	response = client.get("/")

	# Condition de test de Pytest
	# On lui demande de vérifier la réponse de Flask
	# avec le 'assert'
	assert response.data == b"Hello world"


# Lancer avec un terminal la commande 'pytest nom_fichier.py'
# pour lancer le test :)

if __name__ == "__main__":
	app.run()