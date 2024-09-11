from math import pi


def areaCirculo(radio):
    return pi * (radio)**2


print(areaCirculo(5))


def volumenCilindro(radio, altura):
    return areaCirculo(radio) * altura


print(volumenCilindro(5, 10))
