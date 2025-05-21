try:
    lista = [1, 2, 3]
    print(lista[int(input("Indice a mostrar: "))])
except (ValueError, IndexError):
    print("Error: no ingreses letras e ingresa un número dentro del rango.")
