# Definition des routes
# if se trouve dans controller
import flask
import psycopg2
from flask import Blueprint, request, current_app, render_template, make_response, flash

from .logic import check_user_signup, check_email, check_password, check_if_same_password, check_sex, check_orientation, \
    check_update_profil, check_name

blueprint = Blueprint('user', __name__, url_prefix='/')


@blueprint.route("/creer_utilisateur", methods=["POST"])
def creer_utilisateur():
    if not request.cookies.get('user_id'):
        if request.method == 'POST':
            last_name = request.form['last_name']
            first_name = request.form['first_name']
            email = request.form['email']
            password = request.form['password']
            confirm_password = request.form['confirm_password']
            # probleme champs vide avec orientation et sex
            sex = request.form['sex']
            orientation = request.form['orientation']

            if last_name == "" or first_name == "" or email == "" or password == "" or confirm_password == "" or sex == "None" or orientation == "None":
                flash("Vous devez remplir tous les champs.", 'bg-danger')
                return render_template("user/registration.html")

            else:
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
                    if not check_email(email):
                        flash("Il y a une erreur dans votre email.", 'bg-danger')
                        return render_template("user/registration.html")

                    elif not check_password(password):
                        flash("Il y a une erreur dans votre mot de passe. Vérifiez toutes les conditions.", 'bg-danger')
                        return render_template("user/registration.html")

                    elif not check_if_same_password(password, confirm_password):
                        flash("Le mot de passe n'est pas identique.", 'bg-danger')
                        return render_template("user/registration.html")

                    else:
                        flash("Un problème est survenu. Veuillez réessayer.", 'bg-danger')
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
            cur.execute('SELECT id FROM users WHERE email = %s AND password = %s', (email, password,))
            # commit the changes to the database
            result = cur.fetchall()
            # close communication with the database
            cur.close()
            conn.close()

            if result:
                id = result[0][0]
                res = make_response(render_template("homev2.html"))
                res.set_cookie("user_id", value=id)

                return res

            else:
                flash('email ou mot de passe incorrect. Veuillez réessayer !', 'bg-danger')
                return render_template("user/connexion.html")
        else:
            flash('Il faut remplir tous les champs', 'bg-danger')
            return render_template("user/connexion.html")
    else:
        return render_template("homev2.html")


@blueprint.route("/login")
def login():
    if request.cookies.get('user_id'):
        return render_template("homev2.html")
    else:
        return render_template("user/connexion.html")


@blueprint.route("/disconnect")
def disconnect():
    if not request.cookies.get('user_id'):
        return render_template("user/connexion.html")
    else:
        res = make_response(render_template("index.html"))
        res.set_cookie("user_id", "", expires=0)
        return res


@blueprint.route("/signIn")
def sign_in():
    if request.cookies.get('user_id'):
        return render_template("homev2.html")
    else:
        return render_template("user/registration.html")


@blueprint.route("/profile")
def profile():
    if request.cookies.get('user_id'):
        user_id = request.cookies.get('user_id')

        psycopg2_connection_string = current_app.config.get("PSYCOPG2_CONNECTION_STRING")
        # connect to the PostgreSQL database
        conn = psycopg2.connect(psycopg2_connection_string)
        # create a new cursor
        cur = conn.cursor()
        # execute the SELECT statement
        cur.execute('SELECT last_name, first_name, email, bio, sex, orientation FROM users WHERE id = %s;', (user_id,))
        # fetch the data
        result = cur.fetchall()
        cur.close()
        conn.close()
        return render_template("profile.html", result=result)
    else:
        return render_template("user/connexion.html")


@blueprint.route("/modifier_profil", methods=["POST"])
def modifier_profil():
    if request.cookies.get('user_id'):
        if request.method == 'POST':
            user_id = request.cookies.get('user_id')
            last_name = request.form['last_name']
            first_name = request.form['first_name']
            email = request.form['email']
            sex = request.form['sex']
            orientation = request.form['orientation']
            bio = request.form['bio']

            if last_name == "" or first_name == "" or email == "" or sex == "None" or orientation == "None":
                flash("Vous devez remplir tous les champs.", 'bg-danger')
                return render_template("/profil")

            else:
                if check_update_profil(last_name, first_name, email, sex, orientation, bio):
                    sql = """INSERT INTO users(first_name, last_name, email, sex, orientation, bio) VALUES(%s,%s,%s,%s,%s,%s) WHERE id == %s;"""
                    try:
                        psycopg2_connection_string = current_app.config.get("PSYCOPG2_CONNECTION_STRING")
                        conn = psycopg2.connect(psycopg2_connection_string)
                        cur = conn.cursor()
                        cur.execute(sql, (first_name, last_name, email, sex, orientation, bio, user_id))
                        conn.commit()
                        cur.close()
                    except (Exception, psycopg2.DatabaseError) as error:
                        print(error)
                    finally:
                        if conn is not None:
                            conn.close()

                    flash("Votre profil a bien été modifié !", 'bg-success')
                    return render_template("profile.html")
                else:
                    if not check_name(last_name, first_name):
                        flash("Il y a une erreur dans votre nom ou prénom. ils ne doivent pas dépasser 50 charachtère", 'bg-danger')
                        return render_template("profile.html")

                    if not check_email(email):
                        flash("Il y a une erreur dans votre email.", 'bg-danger')
                        return render_template("profile.html")

                    else:
                        flash("Un problème est survenu. Veuillez réessayer.", 'bg-danger')
                        return render_template("profile.html")
        else:
            flash("Un problème est survenu. Veuillez réessayer.", 'bg-danger')
            return render_template("profile.html")
    else:
        return render_template("user/connexion.html")