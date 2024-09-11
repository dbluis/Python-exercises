def aplica_funcion_bool(funcion, lista):

    resultado = []
    for i in lista:
        if funcion(i):
            resultado.append(i)
    return resultado


def par(num):
    return num % 2 == 0


print(aplica_funcion_bool(par, [1, 2, 3, 4, 5, 6]))
