
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




if __name__ == "__main__":
	application.run(host='0.0.0.0', port=80)