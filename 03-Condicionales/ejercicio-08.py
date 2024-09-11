puntos = float(input("Ingrese los puntos del empleado: "))

d = 2400

if (puntos == 0.0):
    print(f"Inaceptable, dinero recivido {d * puntos}")
elif (puntos == 0.4):
    print(f"Aceptable, dinero recivido {d * puntos}")
elif (puntos >= 0.6):
    print(f"Meritorio, dinero recivido {d * puntos}")
else:
    print("Error en el valor de los puntos")
