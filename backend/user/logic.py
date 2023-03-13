import re

# ----------------------------
# Logic for sign in
def check_name(last_name, first_name):
    if len(last_name) == 0 or len(first_name) == 0:
        # raise ValueError("Votre nom ne peut pas être nul")
        return False
    elif last_name.isspace() or first_name.isspace():
        # raise ValueError("Votre nom ne peut pas être blanc")
        return False
    elif len(last_name) > 50 or len(first_name) > 50:
        # raise ValueError("Votre nom ne peut pas excéder 50 caractères")
        return False
    return True


def check_email(email):
    regex = "^[a-zA-Z0-9.!#$%&’*+\/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
    if not re.match(regex, email):
        # raise ValueError("Votre email n'est pas valide")
        return False
    return True


def check_password(password):
    regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,32}$"
    if not re.match(regex, password):
        # raise ValueError("Votre mot de passe n'est pas valide")
        return False
    return True


def check_if_same_password(password, confirm_password):
    if password != confirm_password:
        # raise ValueError("La confirmation de mot de passe n'est pas identique avec votre mot de passe initial")
        return False
    return True


def check_sex(sex):
    if sex != "H" and sex != "F" and sex != "X":
        # raise ValueError("Votre sexe n'est pas valide")
        return False
    return True


def check_orientation(orientation):
    if orientation != "H" and orientation != "F" and orientation != "X" and orientation != "T":
        # raise ValueError("Votre sexe n'est pas valide")
        return False
    return True


def check_user_signup(first_name, last_name, email, password, confirm_password, sex, orientation):
    if check_name(last_name, first_name) and check_email(email) and check_password(password) and check_if_same_password(
            password, confirm_password) and check_sex(sex) and check_orientation(orientation):
        return True
    else:
        return False
        # raise ValueError("Les champs ne sont pas valides")
