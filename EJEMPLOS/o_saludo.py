# Clase Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
              
# Llamar a la Clase y utilizar el método
Persona("Maria","43").saludar()

# Crea intancia de persona
Persona = Persona("Juan","30")

#Accede a los atributos y metodos
print(Persona.nombre) 
print(Persona.edad)
Persona.saludar()