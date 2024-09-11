def cuadrado(num):
    return num * num


def modulo_vector(numeros):
    cuadrados = list(map(cuadrado, numeros))
    return sum(cuadrados) ** (1/2)


print(modulo_vector([1, 2, 2]))
