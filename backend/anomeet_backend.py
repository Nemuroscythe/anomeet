
#######################################################
# Test import
# Comme on est dans un environnement virtuel 
# on peut se permettre d'auto-télécharger les librairies
#
import json
import os
try:
	import flask
	from flask import Response
except:
	os.system("pip install flask")
	import flask

try:
	import psycopg2
except:
	os.system("pip install psycopg2")
	import psycopg2

#######################################################
# Info connection DataBase
# Sur Postgresql - Allwaysdata
#
HOST = "postgresql-test-anomeet.alwaysdata.net"
USER = "test-anomeet_application"
PASSWORD = "Application_Anomeet"
DATABASE = "test-anomeet_postgresql"
PORT = "5432"



#######################################################
# Initialisation Flask
from flask import Flask, request
application = Flask(__name__)


# Route index
@application.route("/")
def index():

	# Connexion à la base de données allwaydata
	with psycopg2.connect(
	            "host=%s dbname=%s user=%s password=%s port=%s" % (HOST, DATABASE, USER, PASSWORD, PORT)) as conn:
	        with conn.cursor() as cur:
	            cur.execute('SELECT * FROM "public"."hello";')
	            data = cur.fetchone()
	
	# A partir d'ici data = une list contenant les infos reçus du serveur
	# idealement il faut faire un print de data -> print(data)
	# pour voir comment les données son organisées sur la table sql
	# ici je sais qu'il me faut data[0]


	return str(data[0])



# Route concernant la reception d'un message
@application.route("/msgSent", methods=["POST"])
def msgSent():
	msg = request.data
	try:
		msg = json.loads(msg)
	except:
		return "-1"

	msg = strip(msg)
	if msg == "" or len(msg) > 512:
		return "-1"

	try:
		with psycopg2.connect(
		            "host=%s dbname=%s user=%s password=%s port=%s" % (HOST, DATABASE, USER, PASSWORD, PORT)) as conn:
		        with conn.cursor() as cur:
		            cur.execute("INSERT INTO message (content) VALUES (%s);", (msg, ))
		            conn.commit()
	except:
		return "-1"
	return "0"






# Routes pour servir l'application "conversation"
@application.route("/conversation", methods=["GET"])
def conversation():
	html = open("../frontend/AM38.html", "r").read()
	return html

@application.route("/AM38.js", methods=["GET"])
def am38_js():
	js = open("../frontend/AM38.js", "r").read()
	return Response(js, mimetype='text/javascript')







if __name__ == "__main__":
	application.run(host='0.0.0.0', port=80)