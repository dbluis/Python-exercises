frutas = {"platano": 1.35, "manzana": 0.80, "pera": 0.85, "naranja": 0.70}

fruta = input("Escriba una fruta: ")
kg = int(input("Escriba la cantidad de kg: "))
total = 0
if fruta in frutas:
    total = frutas[fruta] * kg
    print(f"El precio total de {fruta} es de {total}")
else:
    print("No se encuetra su fruta")
