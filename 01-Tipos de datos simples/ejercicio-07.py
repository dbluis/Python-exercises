altura = float(input("Escriba su altura en Metros: "))

peso = int(input("Escriba su peso: "))

imc = round(peso/altura**2, 2)

print(f"Tu índice de masa corporal es: {imc} ")
