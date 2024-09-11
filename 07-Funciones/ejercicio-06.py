def media(*args):
    total = 0
    for x in args:
        total += x

    return total / len(args)


print(media(2, 2, 2, 1, 2))


def media2(*args):
    return sum(args)/len(args)


print(media2(1, 2, 3, 4, 5, 6))
