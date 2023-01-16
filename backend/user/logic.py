import re


def check_name(last_name, first_name):
    if len(last_name or first_name) > 50:
        raise ValueError("Votre nom ne peut pas excéder 50 charactères")
        #return 2
    elif len(last_name or first_name) == 0:
        raise ValueError("Votre nom ne peut pas être nul")
        #return 3
    elif last_name.isspace() or first_name.isspace():
        raise ValueError("Votre nom ne peut pas être blanc")
        #return 4
    return True


def check_email(email):
    regex = "^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
    if not re.match(regex, email):
        raise ValueError("Votre email n'est pas valide")
    return True


def check_password(password):
    regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,32}$"
    if not re.match(regex, password):
        raise ValueError("Votre mot de passe n'est pas valide")
    return True


def check_if_same_password(password, confirm_password):
    if password != confirm_password:
        raise ValueError("La confirmation de mot de passe n'est pas identique avec votre mot de passe initial")
    return True


def check_sex(sex):
    if sex != "H" and sex != "F" and sex != "X":
        raise ValueError("Votre sexe n'est pas valide")
    return True


def check_user_signup(first_name, last_name, email, password, confirm_password, sex):
    if check_name(last_name, first_name) and check_email(email) and check_password(password) and check_if_same_password(password, confirm_password) and check_sex(sex):
        return True
    else:
        raise ValueError("Les champs ne sont pas valides")
