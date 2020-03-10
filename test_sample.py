from sample import fizzbuzz


def test_fizzbuzz_return():
    assert fizzbuzz(15) == "FizzBuzz"


def test_buzz_return():
    assert fizzbuzz(5) == 'Buzz'