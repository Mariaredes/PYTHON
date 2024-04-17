print("HOLA".lower()) #todo minuscula

print("hola".upper()) #todo mayuscula

print("hola".capitalize()) #solo primera mayuscula


# SINTAXIS DE LA FUNCION

# definición  def: nombre(parametro) return : (retorno)
def saludar(nombre):     
    # codigo de la función
    """print("Hola bienvenido al juego de Cody" )"""
    # retorno de valor
    return "Hola {} ! bienvenid@ al juego de Cody!!".format(nombre)

# ingreso de parametro, variable global
print("Ingresa tu nombre: ")
nombre = input()

# llamdo a la función
print (saludar(nombre))


"""
pueden o no retornar valor
puede o no tener parametros

"""
#definición

def sum(a: int, b: int) -> int:
    """doc: permite sumar 2 numeros enteros.

    Args:
        a (int): N1
        b (int): N2

    Returns:
        int: La suma de a + b
    """
    return a + b

# Llamado a la función 
print(sum(10,20))
print(sum(20,30))
print(sum(40,50))


# sin pasaje de argumentos
def suma():
    a = 10
    b = 11
    resultado = int(a + b)
    return resultado

print(suma())


#con pasaje de argumentos
def resta(a,b):
    resultado = int(a - b)
    return resultado


print(resta(3,13)) 