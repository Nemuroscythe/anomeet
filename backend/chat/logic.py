import json
import psycopg2

HOST = "postgresql-test-anomeet.alwaysdata.net"
USER = "test-anomeet_application"
PASSWORD = "Application_Anomeet"
DATABASE = "test-anomeet_postgresql"
PORT = "5432"

def verification_msg(msg):
    if msg == "" or len(msg) > 512:
        return False

    return True

def retrieveMsg(id_user, id_conversation):
    sql = """SELECT id_person, id, content, date 
             FROM message
             WHERE id_conversation = %s """

    conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s port=%s" % (HOST, DATABASE, USER, PASSWORD, PORT))
    cur = conn.cursor()
    try:
        cur.execute(sql, (id_conversation, ))
        data = cur.fetchall()
    except:
        return "0"

    cur.close()
    conn.close()
    
    return json.dumps(data)
