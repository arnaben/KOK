def add(numbers):
    if numbers == "":
        return 0
    numbers = numbers.replace('\n', ',')
    numbers = [int(n) for n in numbers.split(",") if int(n) <= 1000]
    negative = []
    for n in numbers:
        if n < 0:
            negative.append(str(n))
    if len(negative) > 0:
        raise Exception("Negative numbers not allowed: {}".format(','.join(negative)))

    return sum(numbers)