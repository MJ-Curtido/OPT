from practice18_functions import showList, showElement, addElement, modElement, delElement

products = ["manzanas", "plátanos", "naranjas", "kiwis", "fresas"]
info_shop = ("Frutería La Huerta", "Calle Mayor 12", "912345678", 2010)
prices = {"manzanas": 1.50, "plátanos": 2.10, "naranjas": 1.20, "kiwis": 3.45, "fresas": 2.80}

def listManagement(products):
	print("\n\n")
		
	print("Choose an option:\n\t1. Show list.\n\t2. Show an element.\n\t3. Add element.\n\t4. Modify element.\n\t5. Delete element.\n\t6. Exit.")
	option = int(input("Introduce an option:"))
	
	if option < 1 or option > 4: raise type("IndexError", (IndexError,), {})("Introduce a valid option.")
	
	print("\n")

	match option:
		case 1:
			listManagement(products)
		case 2:
			showElement(products)
		case 3:
			addElement(products)
		case 4:
			print("Goodbye!!")
			keepAsking = False

	print("\n\n")

keepAsking = True

while keepAsking == True:
	try:
		print("\n\n")
		
		print("Choose an option:\n\t1. Show list.\n\t2. Show an element.\n\t3. Add element.\n\t4. Modify element.\n\t5. Delete element.\n\t6. Exit.")
		option = int(input("Introduce an option:"))
		
		if option < 1 or option > 4: raise type("IndexError", (IndexError,), {})("Introduce a valid option.")
		
		print("\n")

		match option:
			case 1:
				listManagement(products)
			case 2:
				showElement(products)
			case 3:
				addElement(products)
			case 4:
				print("Goodbye!!")
				keepAsking = False

		print("\n\n")

	except IndexError:
		print("Error: Index introduced is out of the limits.")
	except ValueError:
		print("Error: Caracter introduced wasn't a number.")
	except Exception as e:
		print(e)
