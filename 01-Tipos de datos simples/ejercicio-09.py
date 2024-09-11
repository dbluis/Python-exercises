cantInvertir = int(input("Escriba la cantidad a invertir: "))

intAnual = int(input("Escriba el '%' de interes:")) / 100

años = int(input("Escriba la cantidad de años: "))

total = cantInvertir + cantInvertir * intAnual * años

print(f"Este es el total de la inversion {total}")
