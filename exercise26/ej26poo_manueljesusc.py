""" Clase Empleado con parámetros nombre y sueldo_base """
class Empleado:
	def __init__(self, nombre, sueldo_base):
		self.nombre = nombre
		self.sueldo_base = sueldo_base
	
	def calcular_sueldo(self):
		return self.sueldo_base

""" Clase Vendedor, que hereda de Empleado y tiene un atributo propio comision """
class Vendedor(Empleado):
	def __init__(self, nombre, sueldo_base, comision):
		super().__init__(nombre, sueldo_base)
		self.comision = comision
	
	def calcular_sueldo(self):
		return self.comision + self.sueldo_base

""" Clase Gerente, que hereda de Empleado y tiene un atributo propio bono_gestion """
class Gerente(Empleado):
	def __init__(self, nombre, sueldo_base, bono_gestion):
		super().__init__(nombre, sueldo_base)
		self.bono_gestion = bono_gestion
	
	def calcular_sueldo(self):
		return self.bono_gestion + self.sueldo_base

employees = [Empleado('Ana', 1200), Vendedor('Carlos', 1200, 350), Gerente('Marta', 2000, 500)]
