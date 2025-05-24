for i in range(3):
    try:
        texto = input("Ingresa una palabra o frase: ")
        if texto == "":
            raise ValueError("La entrada no puede estar vacía.")

        texto_limpio = texto.replace(" ", "").lower()
        if texto_limpio == texto_limpio[::-1]:
            print("Es un palíndromo.")
        else:
            print("No es un palíndromo.")

    except ValueError:
        print("Error: Ingresa una cadena válida")