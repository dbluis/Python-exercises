numero = int(input("Escriba un numero: "))

for i in range(numero + 1):
    if i % 2 == 1:
        print(i, end=", ")

for i in range(1, numero + 1, 2):
    print(i, end=", ")
