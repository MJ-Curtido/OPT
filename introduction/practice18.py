from practice18_functions import show_list, add_element_list, mod_element_list, del_element_list, show_keys_value_dict, add_mod_element_dict, del_element_dict

products = ["manzanas", "plátanos", "naranjas", "kiwis", "fresas"]
info_shop = ("Frutería La Huerta", "Calle Mayor 12", "912345678", 2010)
prices = {"manzanas": 1.50, "plátanos": 2.10, "naranjas": 1.20, "kiwis": 3.45, "fresas": 2.80}

def list_management(products):
	print("\n\n")
		
	print("Choose an option:\n\ta. Consult.\n\tb. Add.\n\tc. Modify.\n\td. Remove.\n\te. Exit.")
	option = input("Introduce an option:")
	
	if option != 'a' and option != 'b' and option != 'c' and option != 'd' and option != 'e': raise type("IndexError", (Exception,), {})("Introduce a valid option.")
	
	print("\n")

	match option:
		case 'a':
			show_list(products)
		case 'b':
			add_element_list(products)
		case 'c':
			mod_element_list(products)
		case 'd':
			del_element_list(products)
		case 'e':
			print('Okay!')

	print("\n\n")

def tuple_consult():
	print(f"- Information about the shop: {info_shop}")
	print(f"Tuple lenght: {len(info_shop)}")
	print(f"Name: {info_shop[0]}")
	print(f"Address: {info_shop[1]}")
	print(f"Phone: {info_shop[2]}")
	print(f"Foundation: {info_shop[3]}")

def show_dict_options(prices):
	option = int(input("Do you want to see the names (1) or the prices (2):"))
	
	if option != 1 and option != 2: raise type("IndexError", (Exception,), {})("Introduce a valid option.")
 
	show_keys_value_dict(prices, option)

def dict_management(prices):
	print("\n\n")
		
	print("Choose an option:\n\ta. Consult.\n\tb. Show.\n\tc. Add/Modify.\n\td. Remove.\n\te. Exit.")
	option = input("Introduce an option:")
	
	if option != 'a' and option != 'b' and option != 'c' and option != 'd' and option != 'e': raise type("IndexError", (Exception,), {})("Introduce a valid option.")
	
	print("\n")

	match option:
		case 'a':
			show_keys_value_dict(prices, 0)
		case 'b':
			show_dict_options(prices)
		case 'c':
			add_mod_element_dict(prices)
		case 'd':
			del_element_dict(prices)
		case 'e':
			keepAsking = False

	print("\n\n")

keepAsking = True

while keepAsking == True:
	try:
		print("\n\n")
		
		print("Choose an option:\n\t1. List Management.\n\t2. Tuple Consult.\n\t3. Dictionary Management.\n\t4. Exit.")
		option = int(input("Introduce an option:"))
		
		if option < 1 or option > 4: raise type("IndexError", (Exception,), {})("Introduce a valid option.")
		
		print("\n")

		match option:
			case 1:
				list_management(products)
			case 2:
				tuple_consult()
			case 3:
				dict_management(prices)
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
