class Foco:

    def __init__(self, color, intensidad, encendido) -> None:
        self.color = color
        self.intensidad = intensidad
        self.encendido = encendido

    def encender(self):
        print("El foco esta encendido")

    def apagar(self):
        print("El foco esta apagado")

foco = Foco('white',250,False)

# muestro los atributos
print(foco.color)
print(foco.intensidad)
print(foco.encendido)

# nuestro los metodos
foco.encender()
foco.apagar()

# HERENCIA
class FocoInteligente(Foco):

    def temporizador(self):
        print('El foco se apagará en 20 min.')


# Instancio objeto
foco2 = FocoInteligente('red',250,True)

# metodos Padre        
foco2.encender()
foco2.apagar()

# metodo Propio
foco2.temporizador()


# HERENCIA MULTIPLE

class Animal:
    def respirar(self):
        print('El animal respira')

class Canino(Animal):
    def ladrar(self):
        print('El perro ladra')

class Mascota(Canino):
    def comer(self):
        print('El perro come sus croquetas')

loki = Mascota()
loki.comer()
loki.ladrar()
loki.respirar()


# Otro ejemplo

