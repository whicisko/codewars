def high_and_low(numbers):
    numbers = [int(x) for x in numbers.split()]
    return str(max(numbers)) + " " + str(min(numbers))


print(high_and_low(12314))
