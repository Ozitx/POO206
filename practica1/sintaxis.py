
# 1. Comentarios
# comentarios de una sola linea

""" aquí va un comentario
de varias lineas
en python """

# 2. strings
print('yo soy otra')

variable1= "hola soy una cadena"
print(len(variable1)) #len guarda el tamaño de la cadena incluyendo los espacios
print(variable1[2:5])
print(variable1[2:])
print(variable1[:5])

# 3. Variables

x= "cynthia"
x= 4
x= 5.67
print(x)

x= int(3)
y= float(3)
z= str(3)

print(x,y,z)
print(type(x)) #lanza cual fue el ultimo tipo de dato que se guardó
print(type(y))
print(type(z))

# 4. Solicitud de datos

a= input("introduce cualquier dato: ")
b= int(input("introduce un numero entero: "))
c= float(input("introduce un numero decimal: "))

# 5. boolean, comparacion y logicos

print(10 > 9)
print(10 < 9)
print(10 == 9)
print(10 >= 9)
print(10 <= 9)
print(10 != 9)

x= 1
print(x<5 and x<10)
print(x<5 or x<10)
print(not(x<5 and x<10))