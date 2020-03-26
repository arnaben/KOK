def add(numbers):
    if numbers == "":
        return 0
    if numbers[0] == '/' and numbers[1] == '/' and '\n' in numbers:
        delim = ''
        for i in range(2, len(numbers)):
            if numbers[i] == '\n':
                break
            else:
                delim += numbers[i]
        numbers = numbers.replace(delim, ',')
        numbers = numbers[3+len(delim):]  # removes the // delimeter and the \n from the start of the numbers
    numbers = numbers.replace('\n', ',')
    numbers = [int(n) for n in numbers.split(",") if int(n) <= 1000]
    negative = []
    for n in numbers:
        if n < 0:
            negative.append(str(n))
    if len(negative) > 0:
        raise Exception("Negative numbers not allowed: {}".format(','.join(negative)))

    return sum(numbers)