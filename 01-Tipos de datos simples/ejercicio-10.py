payasoPeso = 112

muñecaPeso = 75

numPayaso = int(input("Escriba la cantidad de payasos a enviar: "))

numMuñeca = int(input("Escriba la cantidad de muñecas a enviar: "))

pesoTotal = payasoPeso * numPayaso + muñecaPeso * numMuñeca

print(f"Este es el peso total del envio: {pesoTotal/1000}Kg")
