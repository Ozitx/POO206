try:
    numero = int(input("Ingresa un número: "))
    resultado = 2 / numero
except (ValueError, ZeroDivisionError):
    print("Error: ingresa un valor válido")
finally:
    print("Fin del intento :3")
