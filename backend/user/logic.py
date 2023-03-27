import re


def check_name(last_name, first_name):
    if len(last_name) == 0 or len(first_name) == 0:
        return False
    elif last_name.isspace() or first_name.isspace():
        return False
    elif len(last_name) > 50 or len(first_name) > 50:
        return False
    return True


def check_email(email):
    regex = "^[a-zA-Z0-9.!#$%&’*+\/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
    if not re.match(regex, email):
        return False
    return True


def check_password(password):
    regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,32}$"
    if not re.match(regex, password):
        return False
    return True


def check_if_same_password(password, confirm_password):
    if password != confirm_password:
        return False
    return True


def check_sex(sex):
    if sex != "None" and sex != "H" and sex != "F" and sex != "X":
        return False
    return True


def check_orientation(orientation):
    if orientation != "None" and orientation != "H" and orientation != "F" and orientation != "X" and orientation != "T":
        return False
    return True


def check_bio(bio):
    if len(bio) > 500:
        return False
    return True


def check_user_signup(first_name, last_name, email, password, confirm_password, sex, orientation):
    if check_name(last_name, first_name) and check_email(email) and check_password(password) and check_if_same_password(
            password, confirm_password) and check_sex(sex) and check_orientation(orientation):
        return True
    else:
        return False


def check_update_profil(last_name, first_name, sex, orientation, bio):
    if check_name(last_name, first_name) and check_sex(sex) and check_orientation(
            orientation) and check_bio(bio):
        return True
    else:
        return False
