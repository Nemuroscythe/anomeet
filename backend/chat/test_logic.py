import pytest

from .controller import conversation_down
from .logic import *


def random_string(k):
    """Function to generate k length random string for test"""
    import string
    import random

    letters = string.ascii_lowercase
    r = ''.join(random.choice(letters) for i in range(k))

    return r


# Test function
def test_verification_msg_empty_msg():
    assert verification_msg("") == False


def test_verification_msg_long_msg():
    assert verification_msg(random_string(513)) == False


def test_verification_msg_space_only():
    assert verification_msg(" ") == True


def test_verification_msg_good_msg():
    assert verification_msg(random_string(512)) == True

def test_coversation_down():
    assert conversation_down("573a9703-680c-4b88-9c8a-1d5bd32b6230", "573a9703-680c-4b88-9c8a-1d5bd32b6230")

# def test_conversation_up():
#     asse