import pytest

from logic import *

def random_string(k):
    """Function to generate k length random string for test"""
    import string
    import random
    
    letters = string.ascii_lowercase
    r = ''.join(random.choice(letters) for i in range(k))

    return r





# Test function
def test_verification_msg():

    # msg > 512 char
    assert verification_msg(random_string(513)) == False

    # Empty msg
    assert verification_msg("") == False

    # Only space
    assert verification_msg(" ") == True

    # Good string
    assert verification_msg(random_string(512)) == True