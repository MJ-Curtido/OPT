""" Clase Empleado con parámetros nombre y sueldo_base """
class Empleado:
	def __init__(self, nombre: str, sueldo_base: float):
		self.__nombre = nombre
		self.__sueldo_base = sueldo_base
	
	@property
	def nombre(self):
		return self.__nombre
	@nombre.setter
	def nombre(self, value: str):
		if value:
			self.__nombre = value
		else:
			raise ValueError("Name can't be empty")

	@property
	def sueldo_base(self):
		return self.__sueldo_base
	@sueldo_base.setter
	def sueldo_base(self, value: float):
		if value > 0 and value < 200000:
			self.__sueldo_base = value
		else:
			raise ValueError("Base salary must be between 1 € and 199.999 €")
	
	def calcular_sueldo(self):
		return self.sueldo_base

""" Clase Vendedor, que hereda de Empleado y tiene un atributo propio comision """
class Vendedor(Empleado):
	def __init__(self, nombre: str, sueldo_base: float, comision: float):
		super().__init__(nombre, sueldo_base)
		self.__comision = comision

	@property
	def comision(self):
		return self.__comision
	@comision.setter
	def comision(self, value: str):
		if value < self.sueldo_base / 2:
			self.__comision = value
		else:
			raise ValueError("Comision must be lower than 50% of base salary")
	
	def calcular_sueldo(self):
		return self.comision + self.sueldo_base

""" Clase Gerente, que hereda de Empleado y tiene un atributo propio bono_gestion """
class Gerente(Empleado):
	def __init__(self, nombre: str, sueldo_base: float, bono_gestion: float):
		super().__init__(nombre, sueldo_base)
		self.__bono_gestion = bono_gestion

	@property
	def bono_gestion(self):
		return self.__bono_gestion
	@bono_gestion.setter
	def bono_gestion(self, value: str):
		if value:
			self.__bono_gestion = value
		else:
			raise ValueError("Bono management must be lower than 50% of base salary")
	
	def calcular_sueldo(self):
		return self.bono_gestion + self.sueldo_base

if __name__ == '__main__':
	try:
		seller = Vendedor('Carlos', 1200, 350)
		manager = Gerente('Marta', 2000, 500)

		seller.comision = 100
		manager.sueldo_base = -777

		print(seller.comision)
		print(manager.sueldo_base)
	except ValueError as e:
		print(e)
