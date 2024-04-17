# LISTAS:

# Creando listas numéricas en un rango (no toma el maximo valor)
for numero in range(1,6):
    print(numero)

# Creando listas numericas con la funcion list

numeros = list (range(1,6))
print(numeros)

# Creando listas numericas pares

numeros_pares = list(range(2,11,2)) #valor inicial - valor final - paso
print(numeros_pares)

# Creando listas de numeros al cuadrado

numeros_al_cuadrado = []
for valor in range(1,11):
    numeros_al_cuadrado.append(valor**2)
print(numeros_al_cuadrado)

# Obtener valores max, min, y suma de una lista

digitos = [1,2,3,4,5,6,7,8,9,0]
print(min(digitos))
print(max(digitos))
print(sum(digitos))