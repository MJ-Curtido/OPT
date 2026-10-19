# Práctica: Sistema de Gestión y Resumen de Ventas de Vehículos

# Objetivo:
# Se trata de desarrollorar una aplicación para gestionar el registro de ventas de un
# concesionario de coches desde el año 2024 hasta la actualidad. Tendremos unos datos
# iniciales de ventas para tener volumen y permitiremos que el usuario introduzca nuevos
# registros de ventas (con los datos: Marca, Modelo, AñoVenta, AñoFabricacion y precio) y
# pueda visualizar 3 tipos de resúmenes de ventas.

from practica22_data import MARCAS_MODELOS, ventas
from practica22_functions import newSell, sellReport

fruits = ['apple', 'banana', 'orange']

keepAsking = True

while keepAsking == True:
	try:
		print("\n\n")

		print('==========================================')
		print('\tSISTEMA DE GESTIÓN DE VENTAS')
		print('==========================================')
		
		print("\n\n\t1.- Dar de alta una nueva venta\n\t2.- Resumen de ventas (Marca_Modelo_Año)\n\t3.- Resumen de ventas (Marca_Modelo - Todos los años)\n\t4.- Resumen de ventas (Marca - Todos los modelos y años)\n\t5.- Salir del programa")
		option = int(input("Introduce una opcion:"))
		
		if option < 1 or option > 5: raise type("valueException", (Exception,), {})("Introduce una opción válida.")
		
		print("\n")

		match option:
			case 1:
				newSell(MARCAS_MODELOS, ventas)
			case 2:
				sellReport(ventas)
			case 3:
				print()
			case 4:
				print()
			case 5:
				print("Hasta luego!!")
				keepAsking = False

		print("\n\n")

	except ValueError:
		print("Error: Caracter introducido no es un número.")
	except Exception as e:
		print(e)
