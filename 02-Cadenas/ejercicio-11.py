producto = input("Nombre del producto: ")

precio = int(input("Precio del producto: "))

unidades = int(input("Cantidad de unidades: "))

print(f"{producto.capitalize()} tiene un precio de {precio}")

print(f"Y el valor de todas las unidades es de {precio * unidades}")
