def descending_order(num):
    return int("".join(sorted([num for num in str(num)], reverse=True)))


print(descending_order(325386))
