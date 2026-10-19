from practica22_data import MIN_YEAR_FAB, MIN_YEAR_SELL, MAX_YEAR_SELL, MIN_PRICE, MAX_PRICE

def newSell(marcas, ventas):
	try:
		for marca in marcas:
			print('- ', marca)

		inputMarca = input('Introduce una marca: ')
		marca = ''
		modelos = []

		for clave, valor in marcas.items():
			if inputMarca.capitalize().strip() == clave.capitalize().strip():
				modelos = valor
				marca = clave

		if len(modelos) < 1:
			raise type("ValueError", (Exception,), {})("Marca incorrecta.")

		print('\n\n')

		for modelo in modelos:
			print('- ', modelo)

		inputModelo = input('Introduce un modelo: ')
		modelo = ''
		for element in modelos:
			if inputModelo.capitalize().strip() == element.capitalize().strip():
				modelo = element

		if (modelo == ''):
			raise type("ValueError", (Exception,), {})("Modelo incorrecto.")

		yearSell = int(input(f'Introduce el año de venta ({MIN_YEAR_SELL}-{MAX_YEAR_SELL}): '))
		print(yearSell)
		if yearSell > MAX_YEAR_SELL or yearSell < MIN_YEAR_SELL: raise type("ValueError", (Exception,), {})("Introduce una opción válida.")

		yearFab = int(input(f'Introduce el año de fabricación ({MIN_YEAR_FAB}-{yearSell}): '))
		if yearFab > yearSell or yearFab < MIN_YEAR_FAB: raise type("ValueError", (Exception,), {})("Introduce una opción válida.")

		price = float(input(f'Introduce el precio del coche ({MIN_PRICE}-{MAX_PRICE}): '))
		if price > MAX_PRICE or price < MIN_PRICE: raise type("ValueError", (Exception,), {})("Introduce una opción válida.")

		ventas.append([marca, modelo, yearSell, yearFab, price])
		print('Venta registrada correctamente.')
	except Exception as e:
		print(e)

# Esta función tiene 3 variantes, 1 (marca_modelo_añoVenta), 2 (marca_modelo), 3 (marca)
def sellReport(ventas, option):
	try:
		salesDic = {}

		for element in ventas:
			sale = f'{element[0]}_{element[1]}_{element[2]}' if option == 1 else f'{element[0]}_{element[1]}' if option == 2 else f'{element[0]}'
			
			if sale in salesDic:
				salesDic[sale][0] += 1
				salesDic[sale][1] += element[4]
			else:
				salesDic[sale] = [1, element[4]]

		for key, value in salesDic.items():
			print(f'- {key}:')
			print(f'\tUnidades vendidas: {value[0]}')
			print(f'\tEuros acumulados: {value[1]}€\n')
	except Exception as e:
		print(e)