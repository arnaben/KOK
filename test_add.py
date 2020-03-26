from add_functioon import add

def test_empty():
    assert add("") == 0

def test_one_number():
    assert add("1") == 1

test_empty()
test_one_number()