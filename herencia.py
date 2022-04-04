# Ejemplo de herencia

class Empleado:
	def __init__(self, nombre, edad, legajo, sueldo):		# Atributos de la clase padre
		self.nombre = nombre
		self.edad = edad
		self.legajo = legajo
		self.sueldoBase = sueldo

	def calcularSueldo(self, descuentos, bonos):
		return self.sueldoBase - descuentos + bonos
"""
Al poner otra clase como argumento se heredan todos los métodos de la clase padre. Si se redefine un método entonces este será
exclusivo de la clase hija.
"""
class AgenteVentas(Empleado):									# Hereda de la clase empleado
	def __init__(self, nombre, edad, legajo, sueldo, mostrador):
		self.numeroMostrador = mostrador
		super().__init__(nombre, edad, legajo, sueldo)			# Necesario para heredar el constructor de la clase padre


pedro = AgenteVentas("Pedro Martínez", 32, "A120", 55000, 4)
print(pedro.nombre)
print(pedro.calcularSueldo(100, 3000))