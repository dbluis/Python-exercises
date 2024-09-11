import math


def media(*args):
    return sum(args) / len(args)


def varianza(*args):
    total = 0
    for i in args:
        total += (i - media(*args))**2
    return (total / len(args))


def registro(*args):
    calculos = {}
    calculos["media"] = media(*args)
    calculos["varianza"] = varianza(*args)
    calculos["desviacion"] = math.sqrt(varianza(*args))
    return calculos


print(registro(1500, 1200, 1700, 1300, 1800))
