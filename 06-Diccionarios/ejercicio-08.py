palabras = input(
    "Ingrese las palabras separadas por , y : (español:ingles, ...): ").split(",")
traduccion = {}

for i in palabras:
    x = str(i).split(":")
    clave = x[0]
    valor = x[1]
    traduccion[clave] = valor

print(traduccion)
texto = input("Ingrese el texto que desea traducir: ").split(" ")

for j in texto:
    if j in traduccion:
        print(traduccion[j], end=" ")
    else:
        print(j, end=" ")
