def showList(list):
	print('Fruits:\n')

	for element in list:
		print(element)

def showElement(list):
	number = int(input('Introduce a number:'))

	if (number > 0 and number <= len(list)):
		print(number, 'º element: ', list[number - 1])
	else:
		print('There is no element in that number.')

def addElement(list):
	fruit = input('Introduce the name of a fruit:')

	if (fruit):
		list.append(fruit)
		print('Fruit successful added.')
	else:
		print('Invalid fruit.')

