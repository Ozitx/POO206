for i in range(5):
    try:
        valor = int(input("Ingresa un numero positivo entero: "))
        if valor < 0:
            print("El valor debe ser positivo")
        else:
            for i in range(valor, -1, - 1):
                if i > 0:
                    print(i,end=",")
                else:
                    print(i)    
    except ValueError:
        print("Error: No se permiten ese tipo de caracteres, lo siento.")        