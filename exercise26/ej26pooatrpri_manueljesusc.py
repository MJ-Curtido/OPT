""" Clase Empleado con parámetros nombre y sueldo_base """
class Empleado:
	def __init__(self, nombre: str, sueldo_base: float):
		self.__nombre = nombre
		self.__sueldo_base = sueldo_base

	def get_nombre(self):
		return self.__nombre
	def set_nombre(self, value: str):
		if value:
			self.__nombre = value
		else:
			raise ValueError("Name can't be empty")

	def get_sueldo_base(self):
		return self.__sueldo_base
	def set_sueldo_base(self, value: float):
		if value > 0 and value < 200000:
			self.__sueldo_base = value
		else:
			raise ValueError("Base salary must be between 1 € and 199.999 €")
	
	def calcular_sueldo(self):
		return self.get_sueldo_base()

""" Clase Vendedor, que hereda de Empleado y tiene un atributo propio comision """
class Vendedor(Empleado):
	def __init__(self, nombre: str, sueldo_base: float, comision: float):
		super().__init__(nombre, sueldo_base)
		self.__comision = comision

	def get_comision(self):
		return self.__comision
	def set_comision(self, value: str):
		if value < self.get_sueldo_base() / 2:
			self.__comision = value
		else:
			raise ValueError("Comision must be lower than 50% of base salary")
	
	def calcular_sueldo(self):
		return self.get_comision() + self.get_sueldo_base()

""" Clase Gerente, que hereda de Empleado y tiene un atributo propio bono_gestion """
class Gerente(Empleado):
	def __init__(self, nombre: str, sueldo_base: float, bono_gestion: float):
		super().__init__(nombre, sueldo_base)
		self.__bono_gestion = bono_gestion

	def get_bono_gestion(self):
		return self.__bono_gestion
	def set_bono_gestion(self, value: str):
		if value:
			self.__bono_gestion = value
		else:
			raise ValueError("Bono management must be lower than 50% of base salary")
	
	def calcular_sueldo(self):
		return self.get_bono_gestion() + self.get_sueldo_base()

if __name__ == '__main__':
	try:
		seller = Vendedor('Carlos', 1200, 350)
		manager = Gerente('Marta', 2000, 500)

		seller.set_comision(100)
		manager.set_sueldo_base(-777)

		print(seller.get_comision())
		print(manager.get_sueldo_base())
	except ValueError as e:
		print(e)
