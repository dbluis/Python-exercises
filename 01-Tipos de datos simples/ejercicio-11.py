plata = int(input("Ingrese cuanto dinero quiere depositar: "))

tiempo = int(input("Ingrese la cantidad de años que va a depositarlo: "))


def total(monto, años, intereses):
    if años == 1:
        return monto + monto * intereses
    else:
        return monto * intereses + total(monto, años - 1, interes)


print(round(total(plata, tiempo, 0.04), 2))


# Solucion de la pagina

inversion = float(input("Introduce la inversión inicial: "))
interes = 0.04
balance1 = inversion * (1 + interes)
print("Balance tras el primer año:" + str(round(balance1, 2)))
balance2 = balance1 * (1 + interes)
print("Balance tras el segundo año:" + str(round(balance2, 2)))
balance3 = balance2 * (1 + interes)
print("Balance tras el tercer año:" + str(round(balance3, 2)))
