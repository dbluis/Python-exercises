sexo = input("Usted es H - Hombre o M - Mujer: ").upper()

nombre = input("Ingrese su nombre: ").upper()

if ((sexo[0] == "H" and nombre[0] > "N") or (sexo[0] == "M" and nombre[0] < "M")):
    print("Pertenece al grupo A")
else:
    print("Pertenece al grupo B")
