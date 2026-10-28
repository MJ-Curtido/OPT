def show_list(elements):
	print('Fruits: ')

	for i, value in enumerate(elements, 1):
		print(f'{i}. {value}')

def add_element_list(elements):
	fruit = input('Introduce the name of a fruit: ')

	if (fruit and fruit not in elements):
		elements.append(fruit)
		print('\n\nFruit added successfully.')
	else:
		print('\n\nInvalid fruit.')

def mod_element_list(elements):
	show_list(elements)

	print('\n\n')

	try:
		index = int(input('Introduce the position of the fruit you want to modify: '))
		fruit = input('Introduce the name of a fruit: ')

		if (index > 0 and index <= len(elements) and fruit):
			elements[index - 1] = fruit

			print('\n\nFruit modified successfully.')
		else:
			print('\n\nThere is no fruit in that number.')
	except Exception as e:
		print('Introduce a correct value.')

def del_element_list(elements):
	show_list(elements)

	print('\n\n')

	try:
		index = int(input('Introduce the position of the fruit you want to delete: '))

		if (index > 0 and index <= len(elements)):
			fruit = elements.pop(index - 1)

			print('\n\nFruit deleted successfully.')
		else:
			print('\n\nThere is no element in that number.')
	except Exception as e:
		print('Introduce a correct value.')

def show_keys_value_dict(elements, option):
	""" 0: all - 1: keys - 2: values """
	match option:
		case 1:
			print('Fruits: ')

			for i, element in enumerate(elements.keys(), 1):
				print(f'{i}. {element}')
		case 2:
			print('Prices: ')

			for i, value in enumerate(elements.values(), 1):
				print(f'{i}. {value}')
		case _:
			print('Fruits: ')

			for i, (key, value) in enumerate(elements.items(), 1):
				print(f'{i}. {key} - {value} €')

def add_mod_element_dict(elements):
	try:
		fruit = input('Introduce a name of a fruit: ')
		price = int(input('Introduce the price of that fruit: '))

		if fruit and price >= 0:
			elements[fruit] = price

			print('\n\nEverythig have gone successfully.')
		else:
			print('Introduce a correct value.')
	except Exception as e:
		print('Introduce a correct value.')

def del_element_dict(elements):
	show_keys_value_dict(elements, 'key')

	print('\n\n')

	try:
		fruit = input('Introduce the fruit you want to delete: ')

		if (fruit and fruit in elements):
			elements.pop(fruit)

			print(f'\n\n{fruit.capitalize()} deleted successfully.')
		else:
			print('Introduce a correct value.')
	except Exception as e:
		print('Introduce a correct value.')
