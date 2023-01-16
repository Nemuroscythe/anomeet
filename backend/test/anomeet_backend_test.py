import pytest


def test_last_name_empty():
    with pytest.raises(Exception) as e_info:
        last_name = "john"
        first_name = "doe"
        email = "JohnDoe@anonymous.com"
        password = "JohnDoe007"
        # Users(last_name, first_name, email, password)


def test_email_invalid():
    with pytest.raises(Exception) as e_info:
        last_name = "John"
        first_name = "Doe"
        email = "John.anonymous.com"
        password = "JohnDoe007"
        # Users(last_name, first_name, email, password)
