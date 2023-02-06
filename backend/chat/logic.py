def verification_msg(msg):
    if msg == "" or len(msg) > 512:
        return False

    return True

def retrieveMsg(id_user, id_conversation):
    sql = "SELECT id_person, id, content, date FROM message JOIN conversation ON "