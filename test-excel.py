import openpyxl

#
# Open the workbook and extract a sheet by name or the first sheet
#
workbook = openpyxl.load_workbook("test.xlsx", data_only=True, read_only=True)
areas = workbook['Areas']
motorways = workbook['Motorways']

for row in areas:
    print([cell.value for cell in row])

for row in motorways:
    print([cell.value for cell in row])
