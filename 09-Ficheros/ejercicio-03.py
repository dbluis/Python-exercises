def leer_tabla_mult(n, m):
    try:
        with open(f"09-Ficheros/tabla_de_multiplicar_{n}.txt", "r", encoding="utf-8") as f:
            lineas = f.readlines()
            for idx, linea in enumerate(lineas):
                if idx == m:
                    print(linea)
    except (FileNotFoundError):
        print("Fichero no encontrado de la tabla ", n)


leer_tabla_mult(8, 5)
