
# List Comprehesion = mas rapido que el for convencional
# Al generar nuevas listas

# visualizarnumeros positivos
new_numbers = [number for number in numbers if number > 0]

print(
    new_numbers
)

new_numbers = []

for element in numbers:
    if element > 0:
        print(element)


# Generar lista 100 numeros aleatorios
# Conocer cuantas veces se encuentra el numero 50
# Conocer la suma total de todos los elementos

            #valor a guardar    #cuantas veces = iterar 100 veces
numbers = [randint(0,100) for x in range(0,100)] 

#filtro genera una lista si se cumple una condicion

            #Que       #cuanto              #cuando     
numbre_50 = [number for number in numbers if number==50 ] 

result = sum(numbers) #todos los elementos
average = sum(numbers) / len(numbers) #longitud = cant de elementos de la coleccion

        #     0        1       2      3
courses = ['Python','Django','Ruby','Rust'] # Len = 4 
        #    -4       -3       -2    -1       


#Se cuantas veces se va iterar de antemano
#SI conocemos veces
for course in courses:
    print(course)

    count +=1

print(count)

#NO conocemos veces
index = 0
while index < len(couses):
    print(courses[index])

    index += 1  

# Tuplas = son inmutables, no crecen, no se eliminan elementos
# salvaguara informacion es solo de lectura y utilidad para operaciones
#settings =



# Diccionarios -> Llave/valor


# String , Enteros, Flotantes, Booleanos, Tuplas


# Colecciones  (Numpys , Panda y Polars)