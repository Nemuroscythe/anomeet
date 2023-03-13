import pytest
from .logic import *


# Si ça fonctionne
# Si ne fonctionne pas

def test_is_first_name_is_empty():
    assert check_name("", "etet") == False


def test_is_last_name_is_empty():
    assert check_name("etet", "") == False


def test_is_sex_is_empty():
    assert check_sex("") == False


def test_is_email_is_empty():
    assert check_email("") == False


def test_is_password_is_empty():
    assert check_password("") == False


def test_is_same_password_is_empty_password1():
    assert check_if_same_password("", "efe") == False


def test_is_same_password_is_empty_password2():
    assert check_if_same_password("efe", "") == False


def test_check_name_when_true_length_50():
    assert check_name("Jean-Mich", "Dupont") == True


def test_check_name_when_false_length_50():
    assert check_name("Jean-MichJean-MichJean-MichJean-MichJean-MichJean-MichJean-Mich",
                      "DupontDupontDupontDupontDupontDupontDupontDupontDupont") == False


def test_check_name_when_true_empty():
    assert check_name("Jean-Mich", "Dupont") == True


def test_check_name_when_false_empty():
    assert check_name(" ", "") == False


def test_check_name_when_true_isspace():
    assert check_name("Jean-Mich", "Dupont") == True


def test_check_name_when_false_isspace():
    assert check_name(" ", " ") == False


def test_check_email_when_true_regex():
    assert check_email("jean-mich@dupont.fr") == True


def test_check_email_when_false_regex():
    assert check_email("jeanmich.fr") == False


def test_check_password_when_true_regex():
    assert check_password("Azertyuiop123#@") == True


def test_check_password_when_false_regex():
    assert check_password("Azertyuiop123#@^") == False


def test_check_if_same_password():
    assert check_if_same_password("bonmdp", "bonmdp") == True


def test_check_if_same_password_with_different_passwords():
    assert check_if_same_password("bonmdp", "mauvaismdp") == False


def test_check_sex_true():
    assert check_sex("H") == True


def test_check_sex_false():
    assert check_sex("P") == False


def test_check_orientation_true():
    assert check_orientation("H") == True


def test_check_orientation_false():
    assert check_orientation("M") == False


def test_check_user_signup_true():
    assert check_user_signup("Jean-Mich", "Dupont", "jean-mich@dupont.fr",
                             "Azertyuiop123@#", "Azertyuiop123@#", "X", "X") == True


def test_check_user_signup_false():
    assert check_user_signup(" ", "", "jeanmich.fr", "Azertyuiop123", "Azertyuiop12", "Q", "P") == False
