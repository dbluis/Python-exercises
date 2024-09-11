# Mi respuesta

palabra = input("Escriba una palabra: ")

contadorA = 0
contadorE = 0
contadorI = 0
contadorO = 0
contadorU = 0


for i in palabra:
    if i == "a":
        contadorA += 1
    elif i == "e":
        contadorE += 1
    elif i == "i":
        contadorI += 1
    elif i == "o":
        contadorO += 1
    elif i == "u":
        contadorU += 1

print(f"La cantidad de vocales que tiene la palabra es: A={contadorA}, E={
      contadorE}, I={contadorI}, O={contadorO}, U={contadorU}")

# Respuesta:

word = input("Introduce una palabra: ")
vocals = ['a', 'e', 'i', 'o', 'u']
for vocal in vocals:
    times = 0
    for letter in word:
        if letter == vocal:
            times += 1
    print("La vocal " + vocal + " aparece " + str(times) + " veces")
