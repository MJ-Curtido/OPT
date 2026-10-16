from practice17_functions import showList, showElement, addElement, modElement

fruits = ['apple', 'banana', 'orange']

keepAsking = True

while keepAsking == True:
	try:
		print("\n\n")
		
		print("Choose an option:\n\t1. Show list.\n\t2. Show an element.\n\t3. Add element.\n\t4. Modify element.\n\t5. Delete element.\n\t6. Exit.")
		option = int(input("Introduce an option:"))
		
		if option < 1 or option > 14: raise type("valueException", (Exception,), {})("Introduce a valid option.")
		
		print("\n")

		match option:
			case 1:
				showList(fruits)
			case 2:
				showElement(fruits)
			case 3:
				addElement(fruits)
			case 4:
				modElement(fruits)
			case 5:
				delElement() # TODO: Create and add function
			case 6:
				print("Goodbye!!")
				keepAsking = False

		print("\n\n")

	except ValueError:
		print("Error: Caracter introduced wasn't a number.")
	except Exception as e:
		print(e)
