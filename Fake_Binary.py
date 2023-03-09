def fake_bin(x):
    digits = list(x)
    new_digits = []
    for digit in digits:
        if int(digit) < 5:
            new_digits.append('0')
        elif int(digit) >= 5:
            new_digits.append('1')
    digits = ''.join(new_digits)
    return digits