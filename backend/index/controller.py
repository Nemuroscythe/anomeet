import psycopg2
from flask import Blueprint, current_app, render_template
import json

blueprint = Blueprint('index', __name__, url_prefix='/')


@blueprint.route("/")
def index():
    # Connexion à la base de données Alwaysdata
    psycopg2_connection_string = current_app.config.get("PSYCOPG2_CONNECTION_STRING")
    with psycopg2.connect(psycopg2_connection_string) as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM "public"."hello";')
            data = cur.fetchone()
    # À partir d'ici data = une list contenant les infos reçues du serveur
    # idéalement il faut faire un print de data --> print(data)
    # pour voir comment les données sont organisées sur la table sql
    # ici je sais qu'il me faut data[0]
    return render_template("index.html")


# --------------------------------------------------------------------------AM16
# ---------------------------------------------------------------msg on homepage
@blueprint.route("/MainChannelMsg", methods=["POST"])
def retrieveMsg():
    data = {}