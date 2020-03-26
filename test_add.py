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

test_empty()
test_one_number()
test_two_numbers()
test_unknown_amount_of_numbers()
test_newline_delim()