import pytest
from add_functioon import add

def test_empty():
    assert add("") == 0

def test_one_number():
    assert add("1") == 1

def test_two_numbers():
    assert add("1,2") == 3

def test_unknown_amount_of_numbers():
    assert add("1,2,3,4,5") == 15

def test_newline_delim():
    assert add("1\n2,3") == 6

def test_big_numbers():
    assert add("1001,1000") == 1000

def test_negative_numbers():
    with pytest.raises(Exception):
        add("-1,10")

def test_custom_delimiter():
    assert add("//X\n1X2") == 3

test_empty()
test_one_number()
test_two_numbers()
test_unknown_amount_of_numbers()
test_newline_delim()
test_big_numbers()
test_negative_numbers()
test_custom_delimiter()