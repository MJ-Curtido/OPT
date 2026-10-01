# Escribe un programa que pida al usuario su nombre y su apellido, y luego imprima un mensaje de bienvenida que combine ambos.

keepAsking = True

while keepAsking == True:
	try:
		name = input("Introduce your name:")
		if name:
			surname = input("Introduce your surname:")
			if surname:
				print("Welcome", name, surname)

				keepAsking = False
			else: raise type("noValueException", (Exception,), {})("Introduce a valid surname.")
		else: raise type("noValueException", (Exception,), {})("Introduce a valid name.")
	except Exception as e:
		print(e)
