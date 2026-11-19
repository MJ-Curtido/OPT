import pandas as pd

FILE_PATH = "Ej_27_Pandas_1.xlsx"
SHEET_NAME = "Alumnos"
data = {}
data_dict = {}
data_index = {}
data_list = {}

fileDB = pd.ExcelFile(FILE_PATH)
dataframe = pd.read_excel(fileDB, sheet_name=SHEET_NAME, index_col=None)
dataframe.fillna("")
print(dataframe)

""" Opción con orient='records' """
data[SHEET_NAME] = dataframe.to_dict(orient='records')
print("------- RECORDS -------")

for element in data[SHEET_NAME]:
	for key, value in element.items():
		print(f'\t{key}: {value}')
	print('\n---\n')

""" Opción con orient='dict' """
data_dict[SHEET_NAME] = dataframe.to_dict(orient='dict')
print("------- DICT -------")

for column, row in data_dict[SHEET_NAME].items():
	print(f'- {column}')
	for key, value in row.items():
		print(f'\t{key}: {value}')
	print('\n---\n')

""" Opción con orient='index' """
data_index[SHEET_NAME] = dataframe.to_dict(orient='index')
print("------- INDEX -------")

for element in data_index[SHEET_NAME].values():
	for key, value in element.items():
		print(f'\t{key}: {value}')
	print('\n---\n')

""" Opción con orient='list' """
data_list[SHEET_NAME] = dataframe.to_dict(orient='list')
print("------- LIST -------")

for key, value in data_list[SHEET_NAME].items():
	for key, value in element.items():
		print(f'\t{key}: {value}')
	print('\n---\n')
