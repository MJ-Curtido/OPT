from abc import ABC, abstractmethod  

""" Clase abstracta Empleado con método abstracto calcular_sueldo, para que lo tenga que implementar todos sus hijos """
class Empleado(ABC):
	@abstractmethod
	def calcular_sueldo(self) -> float:
		pass

""" Clase EmpleadoBase con parámetros nombre y sueldo_base """
class EmpleadoBase(Empleado):
	def __init__(self, nombre: str, sueldo_base: float):
		self.nombre = nombre
		self.sueldo_base = sueldo_base
	
	def calcular_sueldo(self) -> float:
		return self.sueldo_base

	def __eq__(self, value: EmpleadoBase) -> bool:
		return self.nombre == value.nombre and self.sueldo_base == value.sueldo_base

""" Clase Vendedor, que hereda de Empleado y tiene un atributo propio comision """
class Vendedor(EmpleadoBase):
	def __init__(self, nombre: str, sueldo_base: float, comision: float):
		super().__init__(nombre, sueldo_base)
		self.comision = comision
	
	def calcular_sueldo(self) -> float:
		return self.comision + self.sueldo_base

	def __eq__(self, value: Vendedor) -> bool:
		return self.nombre == value.nombre and self.sueldo_base == value.sueldo_base and self.comision == value.comision

""" Clase Gerente, que hereda de Empleado y tiene un atributo propio bono_gestion """
class Gerente(EmpleadoBase):
	def __init__(self, nombre: str, sueldo_base: float, bono_gestion: float):
		super().__init__(nombre, sueldo_base)
		self.bono_gestion = bono_gestion
	
	def calcular_sueldo(self) -> float:
		return self.bono_gestion + self.sueldo_base

	def __eq__(self, value: Gerente) -> bool:
		return self.nombre == value.nombre and self.sueldo_base == value.sueldo_base and self.bono_gestion == value.bono_gestion

""" Clase Departamento con parámetros nombre, gerente y trabajadores """
class Departamento:
	def __init__(self, nombre: str, gerente: Gerente, trabajadores: list[EmpleadoBase | Vendedor | Gerente]):
		self.nombre = nombre
		self.gerente = gerente
		self.trabajadores = trabajadores

	def transferir_empleado(self, empleado: EmpleadoBase | Gerente | Vendedor, departamento_destino: Departamento) -> None:
		self.trabajadores.remove(empleado)
		departamento_destino.trabajadores.append(empleado)

	def __str__(self):
		text = f"Departamento {self.nombre}"
		text += f"\n - Gerente: {self.gerente.nombre}"
		text += "\n - Trabajadores: "
		for employee in self.trabajadores:
			text += f"\n\t + {employee.nombre} · ({employee.calcular_sueldo()} €)"
		text += "\n\n"

		return text

	def __eq__(self, value: Departamento) -> bool:
		return self.nombre == value.nombre and self.gerente == value.gerente

""" Clase Empresa con parámetros nombre y lista de departamentos """
class Empresa:
	def __init__(self, nombre: str, departamentos: list[Departamento]):
		self.nombre = nombre
		self.departamentos = departamentos

	def agregar_departamento(self, departamento: Departamento) -> None:
		self.departamentos.append(departamento)

	def transferir_empleado(self, empleado: EmpleadoBase | Gerente | Vendedor, departamento_destino: Departamento) -> bool:
		for departamento_origen in self.departamentos:
			for element in departamento_origen.trabajadores:
				if element == empleado:
					departamento_origen.transferir_empleado(element, departamento_destino)
					return True

		return False

	def calcular_nomina_global(self):
		result = 0
		
		for departamento in self.departamentos:
			for empleado in departamento.trabajadores:
				result += empleado.calcular_sueldo()

		return result

	def info_departamentos(self):
		for departamento in self.departamentos:
			print(f"{departamento}\n\n")

if __name__ == '__main__':
	nationalEmployee = EmpleadoBase('Ana', 1200)
	nationalSeller = Vendedor('Carlos', 1200, 350)
	nationalManager = Gerente('Marta', 2000, 500)
	nationalDepartment = Departamento('Nacional', nationalManager, [nationalEmployee, nationalSeller])

	internationalSeller1 = Vendedor('Sarah', 1500, 600)
	internationalSeller2 = Vendedor('Pierre', 1500, 550)
	internationalManager = Gerente('John', 2500, 850)
	internationalDepartment = Departamento('Internacional', internationalManager, [internationalSeller1, internationalSeller2])

	newProductsEmployee = EmpleadoBase('Jaime', 1200)
	newProductsSeller = Vendedor('Secundino', 1200, 350)
	newProductsManager = Gerente('Marta', 2000, 450)
	newProductsDepartment = Departamento('Nuevos Productos', newProductsManager, [newProductsEmployee, newProductsSeller])

	company = Empresa('Secundino S.L.', [nationalDepartment, internationalDepartment])
	company.agregar_departamento(newProductsDepartment)
	if company.transferir_empleado(internationalSeller2, newProductsDepartment):
		print('Employee transfered succesfully.')
	else:
		print('Employee not found.')
	print(f'The global payroll of {company.nombre} is {company.calcular_nomina_global()} €')
	company.info_departamentos()
