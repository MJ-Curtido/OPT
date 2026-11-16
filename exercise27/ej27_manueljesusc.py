import os
import pandas as pd

FILE_PATH = "Ej 27 Pandas 1.xlsx"
SHEET_NAME = "Alumnos"
data = {}
data_dict = {}
data_index = {}

fileDB = pd.ExcelFile(FILE_PATH)
dataframe = pd.read_excel(fileDB, sheet_name=SHEET_NAME, index_col=None)
dataframe.fillna()
print(dataframe)

""" Opción con orient='records' """
data[SHEET_NAME] = dataframe.to_dict(orient='records')
print(data)

for element in data[SHEET_NAME]:
	for key, value in element:
		print(f'\t{key}: {value}')
	print('\n---\n')

""" Opción con orient='dict' """
data_dict[SHEET_NAME] = dataframe.to_dict(orient='dict')
print(data_dict)

for column, row in data_dict[SHEET_NAME].items():
	print(f'- {column}')
	for key, value in row:
		print(f'\t{key}: {value}')
	print('\n---\n')

""" Opción con orient='index' """
data_index[SHEET_NAME] = dataframe.to_dict(orient='index')
print(data_index)

for element in data_index[SHEET_NAME].values():
	for key, value in element:
		print(f'\t{key}: {value}')
	print('\n---\n')
