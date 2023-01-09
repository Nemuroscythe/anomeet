from flask import Flask

application = Flask(__name__)


@application.route("/", methods=["GET"])
def index():
	fichier = open("template/index.html", "r").read()
	fichier = fichier.replace("{test}", "Hello Anomeet")
	return fichier



###
# Autres routes ici...
###


###
# User
exec(open("user/controller.py", "r").read())







"""
Lancement des fichiers statiques
"""
exec(open("static_files.py", "r").read())






"""
Lancement serveur
"""
if __name__ == "__main__":
	application.run()