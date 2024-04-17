#   LISTAS
# Creando listas a partir de objetos iterables

# List comprehesion simple
numeros = [i for i in range(10)]
print(numeros)

cubos = [x**3 for x in range(5)]
print(cubos)

vector = [i for i in range(5)]
print(vector)

# List comprehesion con condicionales

pares = [x for x in range(10) if x%2==0]  # numeros pares
print(pares)

positivos = [num for num in range(-5,5) if num>0] # numeros positivos
print(positivos) 

par_o_impar = ['par' if x%2==0 else 'impar' for x in range(10) ]  # numeros pares o imares
print(par_o_impar)

# List comprehesion anidadas

matriz = [[i for j in range(5)]for i in range(5)] # creacion de matriz 5x5
print(matriz)

lista_anidada = [[1,2,3],[4,5,6],[7,8,9]]  # la tupla no tiene , entre corchete

lista_plana = [elemento for sublista in lista_anidada for elemento in sublista]

print(lista_anidada, lista_plana, sep="\n")

# Comprehension con funciones obtener logitudes de palabras

longitudes = [len(palabra) for palabra in ["gato","ventana","lagrima"]]
print(longitudes)

def cuadrado(x):
    return x**2

cuadrados = [cuadrado(i) for i in range(5)]
print(cuadrados)


