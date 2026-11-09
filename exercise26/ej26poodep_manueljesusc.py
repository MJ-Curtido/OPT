""" Clase Empleado con parámetros nombre y sueldo_base """
class Empleado:
	def __init__(self, nombre: str, sueldo_base: float):
		self.nombre = nombre
		self.sueldo_base = sueldo_base
	
	def calcular_sueldo(self):
		return self.sueldo_base

""" Clase Vendedor, que hereda de Empleado y tiene un atributo propio comision """
class Vendedor(Empleado):
	def __init__(self, nombre: str, sueldo_base: float, comision: float):
		super().__init__(nombre, sueldo_base)
		self.comision = comision
	
	def calcular_sueldo(self):
		return self.comision + self.sueldo_base

""" Clase Gerente, que hereda de Empleado y tiene un atributo propio bono_gestion """
class Gerente(Empleado):
	def __init__(self, nombre: str, sueldo_base: float, bono_gestion: float):
		super().__init__(nombre, sueldo_base)
		self.bono_gestion = bono_gestion
	
	def calcular_sueldo(self):
		return self.bono_gestion + self.sueldo_base

""" Clase Departamento con parámetros nombre, gerente y trabajadores """
class Departamento:
	def __init__(self, nombre: str, gerente: Gerente, trabajadores: list):
		self.nombre = nombre
		self.gerente = gerente
		self.trabajadores = trabajadores

	def __str__(self):
		text = f"Departamento {self.nombre}"
		text += f"\n - Gerente: {self.gerente.nombre}"
		text += "\n - Trabajadores: "
		for employee in self.trabajadores:
			text += f"\n\t + {employee.nombre} · ({employee.calcular_sueldo()} €)"
		text += "\n\n"

		return text

if __name__ == '__main__':
	nationalEmployee = Empleado('Ana', 1200)
	nationalSeller = Vendedor('Carlos', 1200, 350)
	nationalManager = Gerente('Marta', 2000, 500)
	nationalDepartment = Departamento('Nacional', nationalManager, [nationalEmployee, nationalSeller])
	print(nationalDepartment)

	internationalSeller1 = Vendedor('Sarah', 1500, 600)
	internationalSeller2 = Vendedor('Pierre', 1500, 550)
	internationalManager = Gerente('John', 2500, 850)
	internationalDepartment = Departamento('Internacional', internationalManager, [internationalSeller1, internationalSeller2])
	print(internationalDepartment)

	newProductsEmployee = Empleado('Jaime', 1200)
	newProductsSeller = Vendedor('Secundino', 1200, 350)
	newProductsManager = Gerente('Marta', 2000, 450)
	newProductsDepartment = Departamento('Nuevos Productos', newProductsManager, [newProductsEmployee, newProductsSeller])
	print(newProductsDepartment)
