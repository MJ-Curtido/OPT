def newSell(marcas):
	try:
		for marca in marcas:
			print('- ', marca)

		marca = input('Introduce una marca: ')
		modelos = []

		for clave, valor in marcas.items():
			if marca.capitalize() == clave.capitalize():
				modelos = valor

		if len(modelos) < 1:
			print('\nMarca incorrecta.')

		print('\n\n')

		for modelo in modelos:
			print('- ', modelo)

		modelo = input('Introduce un modelo: ')

		for element in modelos.items():
			if modelo.capitalize() == element.capitalize():
				modelo = element

		yearSell = int(input('Introduce un año: '))
		if yearSell <= 2026 or yearSell >= 2024: raise type("ValueError", (Exception,), {})("Introduce una opción válida.")

		yearFab = int(input('Introduce un año: '))
		if yearFab <= yearSell or yearFab >= 1998: raise type("ValueError", (Exception,), {})("Introduce una opción válida.")

	except ValueError:
		print("Error: valor introducido incorrecto")
	except Exception as e:
		print('Error: valor introducido incorrecto')