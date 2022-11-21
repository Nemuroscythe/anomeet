from flask import Flask

application = Flask(__name__)


# Variables globales pour se connecter
# à la base de données Postgres sur alwaysdata
HOST = "postgresql-test-anomeet.alwaysdata.net"
USER = "test-anomeet_application"
PASSWORD = "Application_Anomeet"
DATABASE = "test-anomeet_postgresql"
PORT = "5432"


# J'importe psycopg2, qui est un driver 
# entre Python <-> Postgres
import psycopg2


@application.route("/")
def index():

	# Le driver me demande de créer 2 choses :
	# une connection temporaire
	# et dans cette connection un curseur
	# (Cfr le cours de 2eme de Mr Mbayo)

	# La connection, qu'on initialise avec les variables globales :
	conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s port=%s" % (HOST, DATABASE, USER, PASSWORD, PORT))
	
	# Le curseur à l'intérieur de cette connection :
	cur = conn.cursor()


	# C'est le curseur qui va executer la commande SQL :
	cur.execute('SELECT "content" FROM "public"."hello";')

	# Maintenant le curseur contient l'objet reçu de la base de données
	# qu'il faut convertir, soit en fetchone pour une seule ligne, soit en fetchall pour tout récupérer
	data = cur.fetchone()


	# Comme j'ai fais un 'SELECT *'
	# J'ai reçu toutes les colonnes : le message que l'on veut, et son ID
	# dans une liste accessible par python.
	# Je sais dans mon cas que je veux data[0], mais il est souvent nécessaire
	# de faire un print de cette list afin de savoir dans quel ordre les données
	# sont agencées...
	
	data = data[0]


	# je ferme la connexion
	conn.close()




	# Idem que 02, sauf que je remplace par ce que 
	# j'ai trouvé dans la DB :
	html = open("fichier.html", "r").read()
	html = html.replace("{message}", data)
	return html


application.run()