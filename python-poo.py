# Introducción a clases

"""
class Auto:
	marca = ""			# Atributos
	modelo = 0
	placa = ""

taxi = Auto()

class Nombre:
	pass

victor = Nombre()
maria = Nombre()

# objeto.atributo = valor
"""


class Gato:
	animal = "mamífero"

	def __init__(self, _nombre, _edad):
		self.nombre = _nombre
		self.edad = _edad
		self.alimentos = []

	def verEtapaVida(self):
		if self.edad > 1:
			print(self.nombre, " es adulto.")
		else:
			print(self.nombre, " es cachorro.")

	def esAlimentoFav(self, alimento):
		return alimento in self.alimentos