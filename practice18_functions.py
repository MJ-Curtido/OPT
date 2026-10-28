def showList(elements):
	print('Fruits:\n')

	for element in elements:
		print(element)

def showElement(elements):
	try:
		number = int(input('Introduce a number:'))

		if (number > 0 and number <= len(elements)):
			print(number, 'º element: ', elements[number - 1])
		else:
			print('\n\nThere is no element in that number.')
	except Exception as e:
		print('Introduce a correct value.')

def addElement(elements):
	fruit = input('Introduce the name of a fruit:')

	if (fruit):
		elements.append(fruit)
		print('\n\nFruit added successfully.')
	else:
		print('\n\nInvalid fruit.')

def modElement(elements):
	showList(elements)

	print('\n\n')

	try:
		index = int(input('Introduce the position of the fruit you want to modify:'))
		fruit = input('Introduce the name of a fruit:')

		if (index > 0 and index <= len(elements) and fruit):
			elements[index - 1] = fruit

			print('\n\nFruit modified successfully.')
		else:
			print('\n\nThere is no element in that number.')
	except Exception as e:
		print('Introduce a correct value.')

def delElement(elements):
	showList(elements)

	print('\n\n')

	try:
		index = int(input('Introduce the position of the fruit you want to delete:'))

		if (index > 0 and index <= len(elements)):
			elements.pop(index - 1)

			print('\n\nFruit deleted successfully.')
		else:
			print('\n\nThere is no element in that number.')
	except Exception as e:
		print('Introduce a correct value.')
