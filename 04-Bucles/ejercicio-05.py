capital = int(input("Escriba el capital a invertir: "))

interes = int(input("Escriba el interes anual: "))

años = int(input("Escriba la cantidad de años a invertir: "))

i = 0

while años > i:
    capital *= 1 + interes / 100
    i += 1
    print(f"El total del año {i} es: {round(capital, 2)}")
