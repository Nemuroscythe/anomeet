import re


class Email:
    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, value):
        regex = "^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
        if not re.match(regex, value):
            raise ValueError("Votre email n'est pas valide")
        self.value = value


class Name:
    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, value):
        if len(value) > 50:
            raise ValueError("Votre nom ne peut pas excéder 50 caractères")
        elif len(value) == 0:
            raise ValueError("Votre nom ne peut pas être nul")
        elif value.isspace():
            raise ValueError("Votre nom ne peut pas être blanc")
        self.value = value


class Password:
    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, value):
        # 8 à 32 caractères, au moins une majuscule, 1 minuscule, 1 nombre et un caractère spécial
        regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,32}$"
        if not re.match(regex, value):
            raise ValueError("Votre mot de passe n'est pas valide")
        self.value = value


class Sex:
    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, value):
        if value != "H" and value != "F" and value != "X":
            raise ValueError("Votre sexe n'est pas valide")
        self.value = value

def email(attr):
    def decorator(classe):
        setattr(classe, attr, Email())
        return classe

    return decorator


def first_name(attr):
    def decorator(classe):
        setattr(classe, attr, Name())
        return classe

    return decorator


def last_name(attr):
    def decorator(classe):
        setattr(classe, attr, Name())
        return classe

    return decorator



def password(attr):
    def decorator(classe):
        setattr(classe, attr, Password())
        return classe
    return decorator

def sex(attr):
    def decorator(classe):
        setattr(classe, attr, Sex())
        return classe
    return decorator

@email("email")
@first_name("first_name")
@last_name("last_name")
@password("password")
@sex("sex")

class Users:
    def __init__(self, first_name, last_name, email, password, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.sex = sex
