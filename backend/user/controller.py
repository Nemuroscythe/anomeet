# Definition des routes
# if se trouve dans controller
import psycopg2
from flask import Blueprint, request, current_app, render_template

from .logic import check_user_signup
from .logic import check_user_login

blueprint = Blueprint('user', __name__, url_prefix='/')


@blueprint.route("/recuperer_utilisateur", methods=["GET"])
def recuperer_utilisateur():
    psycopg2_connection_string = current_app.config.get("PSYCOPG2_CONNECTION_STRING")
    # connect to the PostgreSQL database
    conn = psycopg2.connect(psycopg2_connection_string)
    # create a new cursor
    cur = conn.cursor()
    # execute the SELECT statement
    cur.execute('SELECT * FROM users;')
    # fetch the data
    result = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("user/show_user.html", result=result)


@blueprint.route("/creer_utilisateur", methods=["GET"])
def creer_utilisateur():
    if request.method == 'GET':
        last_name = request.args['last_name']
        first_name = request.args['first_name']
        email = request.args['email']
        password = request.args['password']
        confirm_password = request.args['confirm_password']
        sex = request.args['sex']

        if check_user_signup(first_name, last_name, email, password, confirm_password, sex):
            sql = """INSERT INTO users(first_name, last_name, email, password, sex)
                 VALUES(%s,%s,%s,%s,%s);"""
            try:
                psycopg2_connection_string = current_app.config.get("PSYCOPG2_CONNECTION_STRING")
                # connect to the PostgreSQL database
                conn = psycopg2.connect(psycopg2_connection_string)
                # create a new cursor
                cur = conn.cursor()
                # execute the INSERT statement
                cur.execute(sql, (first_name, last_name, email, password, sex))
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
        else:
            return "Erreur"


@blueprint.route("/login_user", methods=["POST"])
def login_user():
    if request.method == 'POST' and request.form['email'] and request.form['password']:
        email = request.form['email']
        password = request.form['password']

        psycopg2_connection_string = current_app.config.get("PSYCOPG2_CONNECTION_STRING")
        # connect to the PostgreSQL database
        conn = psycopg2.connect(psycopg2_connection_string)
        # create a new cursor
        cur = conn.cursor()
        # execute the SELECT statement with email user
        cur.execute('SELECT id FROM users WHERE email = %s AND password = %s', (email, password, ))
        # commit the changes to the database
        result = cur.fetchall()
        # close communication with the database
        cur.close()
        conn.close()

        if result:
            return result
        else:
            return "inscris toi enculé"
    else:
        return "faut remplir les champs"
        # if check_user_login(email, password, result):
#             return


@blueprint.route("/login")
def login():
    html = open("./templates/user/connexion.html", 'r', encoding='utf8').read()
    return html


@blueprint.route("/signIn")
def sign_in():
    html = open("./templates/user/sign_in.html", 'r', encoding='utf8').read()
    return html
