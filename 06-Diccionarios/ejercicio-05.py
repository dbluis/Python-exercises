diccionario = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

contador = 0

for l1, l2 in diccionario.items():
    print(f"La asignatura {l1} tiene un total de creditos de {l2}")
    contador += l2

print(f"El total de creditos es de {contador}")
