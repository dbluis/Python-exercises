print("Hola buen dia tenemos el pan fresco a 3.49$ y el pan de ayer con 60'%' de descuento")

panHoy = int(input("Cuantas barras de pan fresco va a querer? "))

panAyer = int(input("Desea alguna barra de pan de ayer? "))

total = panHoy * 3.49 + panAyer * 3.49 * 60 / 100

print(f"Este es el total: {round(total, 2)}$")
