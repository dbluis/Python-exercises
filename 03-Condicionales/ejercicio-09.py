edad = int(input("ingrese su edad: "))

if edad < 4:
    print("Usted puede pasar gratis ")
elif edad >= 4 and edad < 18:
    print("Usted debe pagar 5$ ")
elif edad >= 18:
    print("Usted debe pagar 10$")
