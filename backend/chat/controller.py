# import des fonctions 
try:
	from logic import *
except:
	from chat.logic import *

# Route concernant la reception d'un message
@application.route("/msgSent", methods=["POST"])
def msg_sent():
	msg = request.data
	try:
		msg = json.loads(msg)
	except:
		return "-1"
	verification_msg(msg)

	try:
		with psycopg2.connect(
		            "host=%s dbname=%s user=%s password=%s port=%s" % (HOST, DATABASE, USER, PASSWORD, PORT)) as conn:
			with conn.cursor() as cur:
				cur.execute("INSERT INTO message (content) VALUES (%s);", (msg, ))
				conn.commit()
	except:
		return "-1"
	return "0"

# Routes pour servir l'application "conversation"
@application.route("/conversation", methods=["GET"])
def conversation():
	html = open("../templates/conversation.html", "r").read()
	return html

@application.route("/conversation.js", methods=["GET"])
def am38_js():
	js = open("../static_files/conversation.js", "r").read()
	return Response(js, mimetype='text/javascript')


if __name__ == "__main__":
	application.run(host='0.0.0.0', port=80)