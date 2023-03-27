import psycopg2
from flask import Blueprint, current_app, render_template, request
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



# ==========================================================================AM16
# ---------------------------------------------------------------msg on homepage
@blueprint.route("/MainChannelMsg", methods=["POST"])
def retrieveMsg():

    data = ()

    sql = """
    SELECT "channelsMessage".id, author, to_char(date, 'DD-MM-YYYY HH24:MI:SS'), channel, content, first_name
    FROM "channelsMessage" JOIN users ON "channelsMessage".author = users.id
    WHERE date >= NOW() - INTERVAL '24 HOURS' 
    ORDER BY date ASC;
    """

    try:
        psycopg2_connection_string = current_app.config.get("PSYCOPG2_CONNECTION_STRING")
        with psycopg2.connect(psycopg2_connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                data = cur.fetchall()
    except Exception as e:
        print(e)
        return "Error SQL"

    canal1 = []
    canal2 = []
    canal3 = []

    #Ordonancement
    try:
        for item in data:
            s = []
            if item[3] == 1:
                s = [item[0], item[1], item[2], item[4], item[5]]
                canal1.append(s)
            elif item[3] == 2:
                s = [item[0], item[1], item[2], item[4], item[5]]
                canal2.append(s)
            elif item[3] == 3:
                s = [item[0], item[1], item[2], item[4], item[5]]
                canal3.append(s)
    except Exception as e:
        print(e)
        return "Error Data"

    #Fabrication de la réponse
    try:
        resp = {"Canal1" : canal1, "Canal2" : canal2, "Canal3" : canal3}
        resp = json.dumps(resp, default=str)
    except Exception as e:
        print(e)
        return "Error making Resp"

    return resp

# ----------------------------------------------------------------------Send msg
@blueprint.route("/MainChannelSend", methods=["POST"])
def sendMsg():
    try:
        data = json.loads(request.data)
    except:
        return "-1"

    try:
        psycopg2_connection_string = current_app.config.get("PSYCOPG2_CONNECTION_STRING")
        with psycopg2.connect(psycopg2_connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute('INSERT INTO "channelsMessage" (channel, author, content) VALUES (%s, %s, %s)', (data[0], data[1], data[2]))
    except Exception as e:
        print(e)
        return "-2"

    return "0"
# ------------------------------------------------------------Retrieve user Name
@blueprint.route("/RetrieveUserName", methods=["POST"])
def retrieveUserName():
    #name = ""
    try:
        data = json.loads(request.data)
    except Exception as e:
        print("Error parsing data")
        print(e)
        return ""

    try:
        psycopg2_connection_string = current_app.config.get("PSYCOPG2_CONNECTION_STRING")
        with psycopg2.connect(psycopg2_connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT first_name FROM users WHERE id = %s", (data,))
                name = cur.fetchone()

    except Exception as e:
        print(e)
        return ""

    try:
        return name[0]
    except Exception as e:
        print(e)
        return ""
# ==============================================================================