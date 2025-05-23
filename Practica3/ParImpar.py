for intento in range(3):
        try:
            numero = int(input("Ingrese un número entero: "))
            if numero % 2 == 0:
                print(f"El número {numero} es par")
            else:
                print(f"El número {numero} es impar")
            break
        except ValueError:
            print("Error: Debe ingresar un número entero válido c:")
            if intento == 3:
                print("Has agotado tus 3 intentos :c")