lista = {}
continuar = "si"
total = 0
while continuar != "no":
    clave = input("Ingrese el producto: ")
    valor = int(input("Ingrese el precio: "))
    lista[clave] = valor
    total += valor
    continuar = input("Desea continuar si/no? ")

print(lista)
print(f"El total es de: {total}")
