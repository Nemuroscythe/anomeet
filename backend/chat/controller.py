import json
import uuid
from random import randrange

import psycopg2
import requests
from flask import Blueprint, request, current_app, Response

from .logic import *

blueprint = Blueprint('chat', __name__, url_prefix='/')


# Route concernant la reception d'un message
@blueprint.route("/msgSent", methods=["POST"])
def msg_sent():
    try:
        msg = json.loads(request.data)
    except Exception as e:
        return str(e)

    if verification_msg(msg):
        psycopg2_connection_string = current_app.config.get("PSYCOPG2_CONNECTION_STRING")
        try:
            with psycopg2.connect(psycopg2_connection_string) as conn:
                with conn.cursor() as cur:
                    cur.execute("INSERT INTO message (content) VALUES (%s);", (msg,))
                    conn.commit()
        except Exception as e:
            return str(e)
    return "0"


# Routes pour servir l'application "conversation"
@blueprint.route("/conversation/<id>", methods=["GET"])
def conversation():
    html = open("templates/chat.html", "r").read()
    return html


@blueprint.route("/conversation.js", methods=["GET"])
def am38_js():
    js = open("templates/chat/conversation.js", "r").read()
    return Response(js, mimetype='text/javascript')


@blueprint.route("/getMsg", methods=["POST"])
def getMsg():
    conversationInfo = request.data
    conversationInfo = json.loads(conversationInfo)
    id_user = conversationInfo["id_user"]
    id_conversation = conversationInfo["id_conversation"]
    listOfMessage = retrieveMsg(id_user, id_conversation)

    return json.dumps(listOfMessage)



@blueprint.route("/start_conversation/<user_one_id>", methods=["GET"])
def create_random_conversation(user_one_id):
    user_one_fullname = get_user_fullname(user_one_id)
    user_two_id = get_random_user()
    user_two_fullname = get_user_fullname(user_two_id)

    conversation_id = create_conversation(user_one_id, user_two_id)

    requests.get("http://127.0.0.1/conversation")
    return "", 301


def create_conversation(user_one_id, user_two_id):
    psycopg2_connection_string = current_app.config.get("PSYCOPG2_CONNECTION_STRING")
    try:
        with psycopg2.connect(psycopg2_connection_string) as conn:
            with conn.cursor() as cur:
                conversation_id = str(uuid.uuid4())
                cur.execute("INSERT INTO conversation(id_conversation, user_one_id, user_two_id) VALUES (%s, %s, %s);",
                            (conversation_id, user_one_id, user_two_id))
            return conversation_id
    except Exception as e:
        return f"Conversation between user: {user_one_id} and user: {user_two_id} could not be created: {str(e)}"


def get_user_fullname(user_id):
    psycopg2_connection_string = current_app.config.get("PSYCOPG2_CONNECTION_STRING")
    try:
        with psycopg2.connect(psycopg2_connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT first_name, last_name FROM users WHERE id = %s;", (user_id,))
                user_data = cur.fetchone()
                return user_data[0] + " " + user_data[1]
    except Exception as e:
        return f"User with id: {user_id} does not exist {str(e)}"


def get_random_user():
    sql = "select id from Users"
    try:
        psycopg2_connection_string = current_app.config.get("PSYCOPG2_CONNECTION_STRING")
        # connect to the PostgreSQL database
        conn = psycopg2.connect(psycopg2_connection_string)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql)
        # commit the changes to the database
        result = cur.fetchall()

        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    random_number = randrange(0, len(result))

    return result[random_number][0]


