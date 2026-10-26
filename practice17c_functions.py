def showList(list):
	print('Fruits:\n')

	for element in list:
		print(element)

def showElement(list):
	try:
		number = int(input('Introduce a number:'))

		if (number > 0 and number <= len(list)):
			print(number, 'º element: ', list[number - 1])
		else:
			print('\n\nThere is no element in that number.')
	except Exception as e:
		print('Introduce a correct value.')

def addElement(list):
	fruit = input('Introduce the name of a fruit:')

	if (fruit):
		list.append(fruit)
		print('\n\nFruit added successfully.')
	else:
		print('\n\nInvalid fruit.')

def modElement(list):
	showList(list)

	print('\n\n')

	try:
		index = int(input('Introduce the position of the fruit you want to modify:'))
		fruit = input('Introduce the name of a fruit:')

		if (index > 0 and index <= len(list) and fruit):
			list[index - 1] = fruit

			print('\n\nFruit modified successfully.')
		else:
			print('\n\nThere is no element in that number.')
	except Exception as e:
		print('Introduce a correct value.')

def delElement(list):
	showList(list)

	print('\n\n')

	try:
		index = int(input('Introduce the position of the fruit you want to delete:'))

		if (index > 0 and index <= len(list)):
			list.pop(index - 1)

			print('\n\nFruit deleted successfully.')
		else:
			print('\n\nThere is no element in that number.')
	except Exception as e:
		print('Introduce a correct value.')
