#######################################################
# Test import
# Comme on est dans un environnement virtuel 
# on peut se permettre d'auto-télécharger les librairies
#######################################################
import os

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
# Sur Postgresql - Allwaysdata
#
HOST = "127.0.0.1"
USER = "test-anomeet_application"
PASSWORD = "Application_Anomeet"
DATABASE = "test-anomeet_Postgresql"
PORT = "5050"

#######################################################
# Initialisation Flask
from flask import Flask, request

application = Flask(__name__)


# Route index
# @application.route("/")
# def index():
#     # Connexion à la base de données allwaydata
#     with psycopg2.connect(
#             "host=%s dbname=%s user=%s password=%s port=%s" % (HOST, DATABASE, USER, PASSWORD, PORT)) as conn:
#         with conn.cursor() as cur:
#             cur.execute('SELECT * FROM "public"."hello";')
#             data = cur.fetchone()
#     # A partir d'ici data = une list contenant les infos reçues du serveur
#     # idealement il faut faire un print de data → print(data)
#     # pour voir comment les données sont organisées sur la table sql
#     # ici je sais qu'il me faut data[0]
#     print("test")
#     return str(data[0])


@application.route("/user", methods=["GET"])
def create_user():
    v1 = 'ali'
    v2 = 'duman'
    v3 = 'ali@duman.be'
    v4 = 'ali'
    conn = psycopg2.connect(
        "host=%s dbname=%s user=%s password=%s port=%s" % (HOST, DATABASE, USER, PASSWORD, PORT))
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Users (first_name, last_name, email, password) VALUES ('ali','duman','ali@duman.be','ali')")
    conn.commit()
    cursor.close()
    conn.close()
    return "Utilisateur créé !"


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=80, debug=True)
