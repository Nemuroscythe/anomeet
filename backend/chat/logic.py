import json
import psycopg2

def verification_msg(msg):
    if msg == "" or len(msg) > 512:
        return False

    return True

def retrieveMsg(id_user, id_conversation):
    sql = """SELECT id_person, id, content, date 
             FROM message
             WHERE id_conversation = %s """

    conn = psycopg2.connect(current_app.config.get("PSYCOPG2_CONNECTION_STRING"))
    cur = conn.cursor()
    cur.execute(sql, (id_conversation, ))

    data = cur.fetchall()
    
    return json.dumps(data)
