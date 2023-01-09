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
@application.route("/")
def index():
    # Connexion à la base de données alwaysdata
    with psycopg2.connect(
            "host=%s dbname=%s user=%s password=%s port=%s" % (HOST, DATABASE, USER, PASSWORD, PORT)) as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM "public"."hello";')
            data = cur.fetchone()
    # À partir d'ici data = une list contenant les infos reçues du serveur
    # idéalement il faut faire un print de data → print(data)
    # pour voir comment les données sont organisées sur la table sql
    # ici je sais qu'il me faut data[0]
    print("test")
    return str(data[0])


@application.route("/create_user", methods=["GET"])
def create_user():
    if request.method == 'GET':
        last_name = request.args['last_name']
        first_name = request.args['first_name']
        email = request.args['email']
        password = request.args['password']
        confirm_password = request.args['confirm_password']
        sex = request.args['sex']

        user = Sign(first_name, last_name, email, password, confirm_password, sex)

        sql = """INSERT INTO users(first_name, last_name, email, password, sex)
             VALUES(%s,%s,%s,%s,%s);"""

    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(
            "host=%s dbname=%s user=%s password=%s port=%s" % (HOST, DATABASE, USER, PASSWORD, PORT))
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (user.first_name, user.last_name, user.email, user.password, user.sex))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return "Utilisateur créé !"


@application.route("/signIn")
def sign_in():
    html = open("../frontend/sign_in.html", 'r', encoding='utf8').read()
    return html


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=80, debug=True)
