"""
Operadores de Comparacion
> mayor que
< menor que
>= mayor o igual que
<= menor o igual que
== igual que
!= diferente que
"""
# Operadores de comparacion

a = 9
b = 14

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


"""
Operadores Lógicos
and
or
not
"""
a = True
b = False

print(a and b)
print(a or b)
print(not a)

"""
Operadores de pertenencia
validar si un numero pertenece a una secuencia o lista

"""
lista = [1,2,3]

print(1 in lista)
print(10 is not lista)


"""
Operadores de identidad
validar si hace referencia a un mismo objeto en memoria

"""

a = [1,2,3]
b = a
c = [1,2,3]

print("estos objetos hacen referencia al mismo espacio en memoria", a is b)
print("estos son objetos distintos", a is c)