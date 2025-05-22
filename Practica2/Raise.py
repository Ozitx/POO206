try:
    x = int(input("Numerador: "))
    y = int(input("Denominador: "))
    
    if y == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    
    resultado = x / y
    print("Resultado:", resultado)

except ZeroDivisionError as e:
    print("Error:", e)
except ValueError:
    print("Entrada inválida. Debes escribir números.")
