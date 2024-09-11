def leer_tabla_mult(n):
    try:
        with open(f"09-Ficheros/tabla_de_multiplicar_{n}.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except (FileNotFoundError):
        print("Fichero no encontrado de la tabla ", n)


leer_tabla_mult(7)
