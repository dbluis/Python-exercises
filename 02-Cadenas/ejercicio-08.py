numero = input("Escriba el precio del producto: ").split(".")

print(
    f"El precio del producto es de {numero[0]} euros con {numero[1]} centavos")

# Otra solucion
# precio = input("Introduce el precio del producto con dos decimales:  ")
# print(precio[:precio.find('.')], 'euros y',precio[precio.find('.')+1:], 'céntimos.')
