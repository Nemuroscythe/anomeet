import json

import psycopg2
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

    if verification_msg(msg) == True:
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
@blueprint.route("/conversation", methods=["GET"])
def conversation():
    html = open("templates/chat/conversation.html", "r").read()
    return html


@blueprint.route("/conversation.js", methods=["GET"])
def am38_js():
    js = open("templates/chat/conversation.js", "r").read()
    return Response(js, mimetype='text/javascript')


@blueprint.route("/start_conversation/<user_one_id>/<user_two_id>", methods=["GET"])
def create_random_conversation(user_one_id, user_two_id):
    user_one_fullname = get_user_fullname(user_one_id)
    user_two_fullname = get_user_fullname(user_two_id)
    return f"{user_one_fullname} and {user_two_fullname} exists"


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
