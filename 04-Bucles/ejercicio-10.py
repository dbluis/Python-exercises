num = int(input("Escriba un numero: "))
contador = 0
for i in range(1, num + 1):
    calculo = num % i
    if calculo == 0:
        contador += 1

    calculo = 0

if contador == 2:
    print("es primo")
else:
    print("no es primo")
