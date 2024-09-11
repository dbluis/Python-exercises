def cuadrados(*args):
    cuadrado = []
    for x in args:
        cuadrado.append(x**2)
    return cuadrado


print(cuadrados(1, 2, 3, 4, 5, 6))
