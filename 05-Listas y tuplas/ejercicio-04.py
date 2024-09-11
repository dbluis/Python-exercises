
num = []
for i in range(6):
    num.append(int(input("Escriba los numero ganadores de la loteria: ")))

num.sort()
print(f"Los numero ganadores son: {num}")
