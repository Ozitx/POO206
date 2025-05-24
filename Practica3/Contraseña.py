for i in range(3):
    contraseña = input("Ingresa una contraseña: ")

    if len(contraseña) < 10:
        print("Contraseña demasiado corta")
    elif not any(c.isdigit() for c in contraseña):
        print("Debe contener al menos un número")
    elif not any(c in "!@#$%&*?" for c in contraseña):
        print("Debe contener al menos un carácter especial")
    else:
        print("Contraseña válida")