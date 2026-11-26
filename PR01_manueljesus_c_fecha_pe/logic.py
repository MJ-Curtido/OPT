import pandas as pd
# import ipdb

FILE_PATH = "PR01_Datos.xlsx"

data = {}

with pd.ExcelFile(FILE_PATH) as xls:
	for sheet in xls.sheet_names:
		df = pd.read_excel(xls, sheet_name=sheet)
		df = df.fillna("")

		data[sheet] = df.to_dict(orient="records") # Diccionario con array de diccionarios

def main():
	print("====================================================================")
	print("SISTEMA DE GESTIÓN ACADÉMICA - INSTITUTO DAW")
	print("====================================================================")
	print("ALERTAS Y ESTADO DEL CENTRO:")
	print("- ALERTA: Faltan alumnos en DAW1 (Actual: 8 / Mínimo: 10).")
	print("- ALERTA: Faltan alumnos en DAW2 (Actual: 8 / Mínimo: 10).")
	print("====================================================================")

if __name__ == '__main__':
	main()
