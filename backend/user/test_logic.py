import pytest
from logic import *


def test_check_name():
    assert check_name("Jean-Mich", "Dupont") == True
    assert check_name(" ", "") == False


def test_check_email():
    assert check_email("jean-mich@dupont.fr") == True
    assert check_email("jeanmich.fr") == False


def test_check_password():
    assert check_password("Azertyuiop123$") == True
    assert check_password("Azertyuiop123") == False


def test_check_if_same_password():
    assert check_if_same_password("bonmdp", "bonmdp") == True
    assert check_if_same_password("bonmdp", "mauvaismdp") == False


def test_check_sex():
    assert check_sex("H") == True
    assert check_sex("P") == False


def test_check_user_signup():
    assert check_user_signup("Jean-Mich", "Dupont", "jean-mich@dupont.fr", "Azertyuiop123$", "Azertyuiop123$",
                             "X") == True
    assert check_user_signup(" ", "", "jeanmich.fr", "Azertyuiop123", "Azertyuiop12", "Q") == False
