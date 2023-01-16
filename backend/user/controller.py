
# Definition des routes
# if se trouve dans controller
from backend.user.logic import check_user_signup


@application.route("/creer_utilisateur", methods=["GET"])
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
                # connect to the PostgreSQL database
                conn = psycopg2.connect(
                    "host=%s dbname=%s user=%s password=%s port=%s" % (HOST, DATABASE, USER, PASSWORD, PORT))
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


@application.route("/signIn")
def sign_in():
    html = open("../frontend/sign_in.html", 'r', encoding='utf8').read()
    return html
