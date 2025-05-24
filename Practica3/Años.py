for i in range(3):
    try:
        año = int(input("\nIngresa un año: "))
        if año < 0:
            print("Error: El año no puede ser negativo")
            break
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            print(f"El año {año} es bisiesto")
        else:
            print(f"El año {año} no es bisiesto")
    except ValueError:
        print("Error: ingrese un año válido por favor :3")