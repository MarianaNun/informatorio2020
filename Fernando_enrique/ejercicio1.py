class Persona:
	def __init__(self, nombre, dni):
		self.nombre = nombre
		self.dni = dni
		self.data = {}
	def __str__(self):
		return "es de clase Persona {}".formar(self.dni)

class Paciente(Persona, Otra_clase):
	def __init__(self,nombre, dni, historia_clinica):
		Persona.__init__(self,nombre,dni)
		self.historia_clinica = historia_clinica
	def __str__(self):
		return "es de clase Paciente {}, dni nro {}".format(self.nombre,self.dni)

Persona1 = Persona( "nelson", 203338643)
Persona2 = Persona( "Gabriel", 39225552)
Paciente1 = Paciente("Lilian", 22665765, "HC N! 1234")
Paciente1 = Paciente("Martin", 42190411, "HC N! 5678")

print(Paciente1.nombre)
print(Paciente1)
print(Persona1)



