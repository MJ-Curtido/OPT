def showList(list):
	print('Fruits:\n')

	for element in list:
		print(element)

def showElement(list):
	number = int(input("Introduce a number:"))

	if (number > 0 and number <= len(list)):
		print(number, 'º element: ', list[number - 1])
	else:
		print('There is no element in that number.')
