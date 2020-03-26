from add_functioon import add

def test_empty():
    assert add("") == 0

def test_one_number():
    assert add("1") == 1

def test_two_numbers():
    assert add("1,2") == 3

test_empty()
test_one_number()
test_two_number()