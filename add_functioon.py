def add(numbers):
    if numbers == "":
        return 0
    numbers = [int(n) for n in numbers.split(",")]

    return sum(numbers)