import pytest
from logic import *

# Si ça fonctionne
# Si ne fonctionne pas


def test_check_name_when_true_length_50():
    assert check_name("Jean-Mich", "Dupont") == True


def test_check_name_when_false_length_50():
    assert check_name("Jean-MichJean-MichJean-MichJean-MichJean-MichJean-MichJean-Mich", "DupontDupontDupontDupontDupontDupontDupontDupontDupont") == False


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
    assert check_password("Azertyuiop123$") == True


def test_check_password_when_false_regex():
    assert check_password("Azertyuiop123") == False


def test_check_if_same_password():
    assert check_if_same_password("bonmdp", "bonmdp") == True


def test_check_if_same_password():
    assert check_if_same_password("bonmdp", "mauvaismdp") == False


def test_check_sex():
    assert check_sex("H") == True
    assert check_sex("P") == False


def test_check_user_signup():
    assert check_user_signup("Jean-Mich", "Dupont", "jean-mich@dupont.fr", "Azertyuiop123$", "Azertyuiop123$",
                             "X") == True
    assert check_user_signup(" ", "", "jeanmich.fr", "Azertyuiop123", "Azertyuiop12", "Q") == False
