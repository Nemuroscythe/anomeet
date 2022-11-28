import re


class Email:
    def __get__(self, obj, objtype=None):
        return self.value

    def __set__(self, obj, value):
        regex="^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        if not re.match(regex, value):
            raise ValueError("Votre email n'est pas valide")
        self.value = value

def email(attr):
    def decorator(classe):
        setattr(classe, attr, Email())
        return classe
    return decorator
#
# def textNotBlank(attr):
#     def decorator(classe):
#         setattr(classe, attr, TextNotBlank())
#         return classe
#     return decorator
#
# def password(attr):
#     def decorator(classe):
#         setattr(classe, attr, Password())
#         return classe
#     return decorator

@email(email)
# @textNotBlank(first_name)
# @textNotBlank(last_name)
# @password(password())
class Users:
    def __init__(self, first_name, last_name, email, password, sexe):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.sexe = sexe
