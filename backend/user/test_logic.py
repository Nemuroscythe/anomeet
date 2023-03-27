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


def test_check_profil_bio_true():
    assert check_bio("bonjour , 0ç! tous ") == True


def test_check_profil_bio_false():
    assert check_bio("Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. "
                     "Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus "
                     "mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa "
                     "quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, "
                     "rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. "
                     "Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend "
                     "tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem "
                     "ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius "
                     "laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur "
                     "ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget "
                     "condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam "
                     "nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt "
                     "tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci "
                     "eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales "
                     "sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, quis gravida "
                     "magna mi a libero. Fusce vulputate eleifend sapien. Vestibulum purus quam, scelerisque ut, "
                     "mollis sed, nonummy id, metus. Nullam accumsan lorem in dui. Cras ultricies mi eu turpis "
                     "hendrerit fringilla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere "
                     "cubilia Curae; In ac dui quis mi consectetuer lacinia. Nam pretium turpis et arcu. Duis arcu "
                     "tortor, suscipit eget, imperdiet nec, imperdiet iaculis, ipsum. Sed aliquam ultrices mauris. "
                     "Integer ante arcu, accumsan a, consectetuer eget, posuere ut, mauris. Praesent adipiscing. "
                     "Phasellus ullamcorper ipsum rutrum nunc. Nunc nonummy metus. Vestibulum volutpat pretium "
                     "libero. Cras id dui. Aenean ut eros et nisl sagittis vestibulum. Nullam nulla eros, "
                     "ultricies sit amet, nonummy id, imperdiet feugiat, pede. Sed lectus. Donec mollis hendrerit "
                     "risus. Phasellus nec sem in justo pellentesque facilisis. Etiam imperdiet imperdiet orci. Nunc "
                     "nec neque. Phasellus leo dolor, tempus non, auctor et, hendrerit quis, nisi. Curabitur ligula "
                     "sapien, tincidunt non, euismod vitae, posuere imperdiet, leo. Maecenas malesuada. Praesent "
                     "congue erat at massa. Sed cursus turpis vitae tortor. Donec posuere vulputate arcu. Phasellus "
                     "accumsan cursus velit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere "
                     "cubilia Curae; Sed aliquam, nisi quis porttitor congue, elit erat euismod orci, ac placerat "
                     "dolor lectus quis orci. Phasellus consectetuer vestibulum elit. Aenean tellus metus, "
                     "bibendum sed, posuere ac, mattis non, nunc. Vestibulum fringilla pede sit amet augue. In "
                     "turpis. Pellentesque posuere. Praesent turpis. Aenean posuere, tortor sed cursus feugiat, "
                     "nunc augue blandit nunc, eu sollicitudin urna dolor sagittis lacus. Donec elit libero, "
                     "sodales nec, volutpat a, suscipit non, turpis. Nullam sagittis. Suspendisse pulvinar, "
                     "augue ac venenatis condimentum, sem libero volutpat nibh, nec pellentesque velit pede quis "
                     "nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; "
                     "Fusce id purus. Ut varius tincidunt libero. Phasellus dolor. Maecenas vestibulum mollis diam.") == False
