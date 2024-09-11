def longitud(frase):
    palabras = {}
    x = frase.split(" ")
    for i in x:
        palabras[i] = len(i)

    return palabras


print(longitud("Hola perro todo bien"))

f = {palabra: len(palabra) for palabra in ['I', 'love', 'Python']}

print(f)
