# Definition des routes
# if se trouve dans controller
import flask
import psycopg2
from flask import Blueprint, request, current_app, render_template, make_response, flash, redirect, url_for

from .logic import check_user_signup

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
    if not request.cookies.get('user_id'):
        if request.method == 'GET':
            last_name = request.args['last_name']
            first_name = request.args['first_name']
            email = request.args['email']
            password = request.args['password']
            confirm_password = request.args['confirm_password']
            sex = request.args['sex']
            orientation = request.args['orientation']

            if check_user_signup(first_name, last_name, email, password, confirm_password, sex, orientation):
                sql = """INSERT INTO users(first_name, last_name, email, password, sex, orientation)
                     VALUES(%s,%s,%s,%s,%s,%s);"""
                try:
                    psycopg2_connection_string = current_app.config.get("PSYCOPG2_CONNECTION_STRING")
                    # connect to the PostgreSQL database
                    conn = psycopg2.connect(psycopg2_connection_string)
                    # create a new cursor
                    cur = conn.cursor()
                    # execute the INSERT statement
                    cur.execute(sql, (first_name, last_name, email, password, sex, orientation))
                    # commit the changes to the database
                    conn.commit()
                    # close communication with the database
                    cur.close()
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
                finally:
                    if conn is not None:
                        conn.close()

                flash("Votre profil a bien été créé !", 'bg-success')
                return render_template("user/connexion.html")
            else:
                flash("Il y a une erreur dans votre formulaire", 'bg-danger')
                return render_template("user/registration.html")
    else:
        flask.abort(403)


@blueprint.route("/login_user", methods=["POST"])
def login_user():
    if not request.cookies.get('user_id'):
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
                id = result[0][0]
                res = make_response()
                res.set_cookie("user_id", value=id)

                return res

            else:
                flash('email ou mot de passe incorrect. Veuillez réessayer !', 'bg-danger')
                return render_template("user/connexion.html")
        else:
            flash('Il faut remplir tous les champs', 'bg-danger')
            return render_template("user/connexion.html")
    else:
        flask.abort(403)


@blueprint.route("/login")
def login():
    if request.cookies.get('user_id'):
        flask.abort(403)
    else:
        return render_template("user/connexion.html")


@blueprint.route("/disconnect")
def disconnect():
    if not request.cookies.get('user_id'):
        flask.abort(403)
    else:
        res = make_response()
        res.set_cookie("user_id", "", expires=0)
        return res


@blueprint.route("/signIn")
def sign_in():
    if request.cookies.get('user_id'):
        flask.abort(403)
    else:
        return render_template("user/registration.html")
