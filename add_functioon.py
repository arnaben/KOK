def add(numbers):
    if numbers == "":
        return 0
    numbers = numbers.replace('\n', ',')
    numbers = [int(n) for n in numbers.split(",") if int(n) <= 1000]

    return sum(numbers)