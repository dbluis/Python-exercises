n = int(input("ingrese un numero: "))

for i in range(n):
    for j in range(i + 1):
        print("*", end="")
    print("")

for i in range(3):
    print("||")
