def frecuencia(texto):
    diccionario = {}
    texto = str(texto).split(" ")
    for palabra in texto:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario


print(frecuencia("hola todo bine hola perro que paso paso paso paso"))


def masRepetida(texto):
    maximo = 0
    palabra = ""
    for i in frecuencia(texto):
        if maximo < frecuencia(texto)[i]:
            maximo = frecuencia(texto)[i]
            palabra = i
    return maximo, palabra


print(masRepetida("hola todo bine hola perro que paso paso paso paso"))
