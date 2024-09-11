def tabla_de_multiplicar(n):
    with open(f"09-Ficheros/tabla_de_multiplicar_{n}.txt", "w", encoding="utf-8") as f:
        f.write(f"-Tabla de multiplicar del numero {n} \n")
        for x in range(1, 11):
            f.write(f" {x} x {n} = {x*n} \n")


tabla_de_multiplicar(8)
