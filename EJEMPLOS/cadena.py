# Cadena simple
print("Esto es una cadena")
print('Esto es también es una cadena')

# Cadena con comillas dobles y simples
print('Le dije a mi amigo, "Python es mi lenguaje favorito"')
print("El lenguaje 'Python' se nombró en honor a Monty Python")


# Cadenas y metodos de cadena (string msth)
titulo= "Esto es un título"
print(titulo.title())
print(titulo.upper())
print(titulo.lower())

# Interpolacion de cadenas
nombre = "Nombre"
apellido = "Apellido"
nombre_completo = f"{nombre} {apellido}"
print(nombre_completo)

# Caracteres de tabulacion
print("\tPython")
print("Lenguajes:\nPython\nC\nJavaScript")

# Devolver longitud de una cadena
len("Hola Mundo")

# Metodos de eliminación de espacios
lenguaje_favorito = 'python  '
print(lenguaje_favorito.rstrip())

# Remover prefijos
url_mostrar='https://noostarth.com'
#print(url_mostrar.removeprefix('https://noostarth.com'))
