from math import pi


def serie_taylor(x, fun):
    if fun == "sen":
        valor = x - ((x**3)/6) + ((x**5)/120) - ((x**7)/5040) + \
            ((x**9) / 362880) - ((x**11) / 39916800)
        return valor
    elif fun == "cos":
        valor = 1 - ((x**2)/2) + ((x**4)/24) - ((x**6)/720) + \
            ((x**8)/40320) - ((x**10)/3628800)
        return valor
    elif fun == "tan":
        valor = x + ((1/3)*(x**3)) + ((2/15)*(x**5)) + \
            ((17/315)*((x**7))) + ((62/2835)*(x**9))
        return valor


def fun_sen(x):
    x = x * (pi/180)
    total = serie_taylor(x, "sen")
    return round(total, 2)


def fun_cos(x):
    x = x * (pi/180)
    total = serie_taylor(x, "cos")
    return round(total, 2)


def fun_tan(x):
    x = x * (pi/180)
    total = serie_taylor(x, "tan")
    return round(total, 2)


def fun_exponencial(num, x):
    total = num ** x
    return total


def ln(x):
    e = 2.718281
    exp = 1
    while True:
        if x > round((e**exp), 3):
            exp += 1
            if x == round((e**exp), 3):
                break

        elif x < round((e**exp), 3):
            exp -= 0.9
            if x == round((e**exp), 3):
                break
            elif x > round((e**exp), 3):
                exp += 0.01
                if x == round((e**exp), 3):
                    break
            elif x < round((e**exp), 3):
                exp -= 0.009
                if x == round((e**exp), 3):
                    break
                elif x > round((e**exp), 3):
                    exp += 0.0001
                    if x == round((e**exp), 3):
                        break
                elif x < round((e**exp), 3):
                    exp -= 0.00009
                    if x == round((e**exp), 3):
                        break

    y1 = exp - (x*((e**exp)-x)) / ((e**exp)+x)
    y2 = y1 - (x*((e**y1)-x)) / ((e**y1)+x)
    return round(y2, 5)


def calculadora():
    print("1 - Calcular sen()\n2 - Calcular cos()\n3 - Calcular tan()\n4 - Calcular exponencial\n5 - Calcular ln()")
    opcion = input("Elija una opcion: ")
    if opcion == "1":
        num = int(input("Ingrese un numero: "))
        return fun_sen(num)
    elif opcion == "2":
        num = int(input("Ingrese un numero: "))
        return fun_cos(num)
    elif opcion == "3":
        num = int(input("Ingrese un numero: "))
        return fun_tan(num)
    elif opcion == "4":
        num = int(input("Ingrese un numero: "))
        exp = int(input("Ahora ingrese su exponente: "))
        return fun_exponencial(num, exp)
    elif opcion == "5":
        num = int(input("Ingrese un numero: "))
        return ln(num)


print(calculadora())
