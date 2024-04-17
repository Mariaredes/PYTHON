# Asignacion multiple de numeros en variables
a,b,c =10,50,600
print(a,b,c,sep="\n")

# Asignacion de constantes
MAX_CONECCIONES = 5000
print(MAX_CONECCIONES)

# Numeros grandes Legibles
suscriptores= 14_000_000_000
print(suscriptores)

# Operaciones
a = 5 #num entero
b = 3 # otro num entero

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
potencia = a ** b
modulo = a % b

print(suma,resta,multiplicacion,division,potencia,modulo, sep="\n")

print("ingresa el primer valor")
num1 = int(input())
print("ingresa el segundo valor")
num2 = int(input())

#Suma
resultado = num1 + num2
print("resultado suma:")
print(resultado)

#Resta
resultado = num1 - num2
print("resultado resta:")
print(resultado)

#Producto
resultado = num1 * num2
print("resultado producto:")
print(resultado)

#Division
resultado = num1 / num2
print("resultado division:")
print(resultado)


#Funcion suma
print("***Funcion Suma***")
def suma(a,b):
    resultado = a+b
    return resultado

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
print(suma(num1,num2))

#Funcion potencia
print("F***Funcion Potencia***")
def potencia(a,b):
    resultado = (pow(a,b))
    return resultado

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
print(potencia(num1,num2))

"""
def suma(a,b):
    a = input("ingrese un numero: ")
    b = input("ingrese un numero: ")
resultado = a + b
return resultado

(suma(5,6))


#Funcion Suma
def sumar():
    a = input("ingrese un numero: ")
    b = input("ingrese un numero: ")
resultado = a+b
print resultado

#print(suma(5,6))
"""