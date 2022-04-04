# Pequeño juego en el que un prota lucha contra enemigos aleatorios

class Protagonista:
	def __init__(self, _nombre, _nivel, _salud, _ataque, _defensa, _exp):
		self.nombre = _nombre
		self.nivel = _nivel
		self.salud = _salud
		self.ataque = _ataque
		self.defensa = _defensa
		self.exp = _exp
		self.ataques = []


class Enemigo:
	
