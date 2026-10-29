EMPRESA_INFO = ("Tech Solutions S.L.", "B-12345678", "Madrid")
departamentos = [["Informatica", 12], ["Recursos Humanos", 4]]
inventario_dict = {"Electronica": [["Televisor", 450.0], ["Movil", 300.0]], "Hogar": [["Microondas", 120.0]]}

option = 0

def add_departamento():
	try:
		name = input("Introduce el nombre del departamento: ")
		name = name.strip().capitalize()
		num = int(input("Introduce el numero de trabajadores: "))

		if name and num > 0:
			is_departamento = False

			for e in departamentos:
				print(e[0],name, e[0] == name)
				if e[0] in name:
					is_departamento = True

			if not is_departamento:
				departamentos.append([name, num])
				print(f"Departamento '{name}' registrado correctamente.\n\n")
			else:
				print(f"Error: El departamento '{name}' ya existe en el sistema.\n\n")
		else:
			print('Introduce una opcion valida.\n\n')
	except Exception as e:
		print('Introduce una opcion valida.\n\n')

def show_departamentos():
	sumatory = 0

	for d in departamentos:
		print(f'Departamento: {d[0]} - Numero de personas: {d[1]}')
		sumatory += d[1]
	
	print(f'TOTAL DE EMPLEADOS EN LA EMPRESA: {sumatory}\n\n')

def show_inventario():
	print("--- INVENTARIO POR DEPARTAMENTOS ---")

	expensive_prod = ["initialice", 0]

	for key, value in inventario_dict.items():
		print(f'Departamento: {key}')

		for i in value:
			print(f"\tProducto: {i[0]} - Precio: {i[1]} €")

			if i[1] > expensive_prod[1]:
				expensive_prod = i
	
	print(f"El producto con mayor precio es: {expensive_prod[0]} con un precio de {expensive_prod[1]} euros.\n\n")

while option != 4:
	try:
		print(f'DATOS EMPRESA: {EMPRESA_INFO[0]} - CIF: {EMPRESA_INFO[1]} - Ciudad: {EMPRESA_INFO[2]}')

		print(f"=== GESTION INTERNA - {EMPRESA_INFO[0]} ===")
		
		print("1. Anadir nuevo departamento")
		print("2. Imprimir: departamentos, numero de personas y el numero total de empleados de la empresa")
		print("3. Imprimir: inventario de productos y el nombre del producto con un precio mayor")
		print("4. Salir")

		option = int(input("Introduce una opcion: "))

		match option:
			case 1:
				add_departamento()
			case 2:
				show_departamentos()
			case 3:
				show_inventario()
			case 4:
				print("Saliendo del sistema de Tech Solutions S.L....")
	except Exception as e:
		print('Introduce una opcion valida.\n\n')
