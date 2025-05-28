for i in range(4):
    try:
        Numero = int(input("\nIngresa un numero entero positivo mayor a 10: "))
        if Numero > 10:
                for i in range(3, Numero + 1):
                    if i % 2 != 0:
                        print(i, end=",")
        else:
            print("El numero debe ser mayor a 10")
            
    except ValueError:
        print("Solo se aceptan números enteros c:")