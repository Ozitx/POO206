for i in range(5):
    try:
        frase = input("Ingresa una frase corta: ")
        letra = input("Ahora ingresa una letra cualquiera: ")
        if len(letra) != 1:
            print("Solo se puede ingresar una letra c:")
        else:
            cantidad = frase.count(letra)
            print("La letra " + letra + " aparece " + str(cantidad) + " veces en la frase que escribiste ")
    except ValueError:
        print("Error: No se aceptan valores de ese tipo :c")