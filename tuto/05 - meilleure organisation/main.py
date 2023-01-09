from flask import Flask

application = Flask(__name__)


@application.route("/", methods=["GET"])
def index():
	return "Hello Anomeet"



###
# Autres routes ici...
###








"""
Lancement des fichiers statiques
"""
exec(open("static_files.py", "r").read())






"""
Lancement serveur
"""
if __name__ == "__main__":
	application.run()