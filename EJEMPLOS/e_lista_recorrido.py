# LISTAS:

# Recorrido de la lista bucle for

frutas= ["manzana","banana","cereza","durazno"]
for fruta in frutas:
    print(fruta)

# Recorriendo una lista y obteniendo el indice

for indice, fruta in enumerate(frutas):
    print(f"Fruta {indice+1}:{fruta}")

# Recorrido de una lista alreves
for fruta in reversed(frutas):
    print(fruta)

# Recorrido de una lista ordenada
for fruta in sorted(frutas):
    print(fruta)