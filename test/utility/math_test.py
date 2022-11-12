import pytest
from main.utility.math import sum

def test_with_positives():
	x=5
	y=6
	assert sum(x, y) == 11

def test_with_negative():
	x=-5
	y=-6
	assert sum(x, y) == -11
