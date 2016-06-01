#Encapsulacion

class Prueba(object):
	def __init__(self):
		self.__privado = "soy privado"
		self.privado = "soy publico"

	def __metodoPrivado(self):
		print "soy privado"

	def metodoPublico(self):
		print "soy publico"

obj = Prueba()

print obj.privado