#######################################################
# Test import
# Comme on est dans un environnement virtuel 
# on peut se permettre d'auto-télécharger les librairies
#######################################################
import os

from backend.users import Users
from backend.sign_in_treatment import Sign

try:
    import flask
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
# Sur Postgresql - Alwaysdata
#
HOST = "postgresql-test-anomeet.alwaysdata.net"
USER = "test-anomeet_application"
PASSWORD = "Application_Anomeet"
DATABASE = "test-anomeet_postgresql"
PORT = "5432"

#######################################################
# Initialisation Flask
from flask import Flask, request, render_template

application = Flask(__name__)


# Route index
###
# User
exec(open("user/controller.py", "r").read())







"""
Lancement des fichiers statiques
"""
exec(open("static_files.py", "r").read())



if __name__ == "__main__":
    application.run(host='0.0.0.0', port=80, debug=True)
