import math
numeros = input("Escriba una cadena de numeros separados por , : ").split(",")

media = 0
desviacion = 0
for i in numeros:
    media += int(i)

media = media / len(numeros)

for i in numeros:
    desviacion += (int(i) - media)**2

desviacion = math.sqrt(desviacion / len(numeros))

print(f"La media es: {media} y la desviacion tipica es: {desviacion}")
