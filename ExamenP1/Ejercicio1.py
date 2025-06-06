for i in range(4):
    try:
        numero = int(input("\nIntroduce un número par entre 200 y 400: "))
        if 200 <= numero <= 400 and numero % 2 == 0:
            break
        else:
            print("El número debe ser par y estar entre 200 y 400.")
    except ValueError:
        print("Entrada inválida, ingresa un número entero.")

print(f"Números pares desde {numero} hasta 400:")
for i in range(numero, 401, 2):
    print(i, end=",")
