print("Desea una pizza vegetariana o no vegetariana?")
pizza = input("Seleccione 1: Vegetariana o 2:No vegetariana: ")

if pizza == "1":
    ingredientes = input("Seleccione 1: Pimiento o 2: Tofu ")
    if ingredientes == "1":
        ing = "Pimiento"
    elif ingredientes == "2":
        ing = "Tofu"
elif pizza == "2":
    ingredientes = input("Seleccione 1: Peperoni, 2: Jamón o 3: Salmón ")
    if ingredientes == "1":
        ing = "Peperoni"
    elif ingredientes == "2":
        ing = "Jamón"
    elif ingredientes == "3":
        ing = "Salmón"

print(f"Su pizza tiene mozzarella, tomate y {ing} ")
