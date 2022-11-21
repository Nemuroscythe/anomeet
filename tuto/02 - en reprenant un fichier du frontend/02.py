from flask import Flask

application = Flask(__name__)

@application.route("/")
def index():

	# J'ouvre mon fichier '.html' issu du frontend
	# que je stock dans une variable
	html = open("fichier.html", "r").read()


	# Dans ce fichier je sais qu'il y a une balise:
	# {message}
	# qui est laissé tel quel dans le but d'etre
	# modifiée par le serveur avant d'être renvoyé
	# au client.
	html = html.replace("{message}", "Hello Anomeet!")


	# une fois ma variable html prete je la renvoie :)
	return html


application.run()