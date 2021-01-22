from openpyxl import load_workbook

filename = r'D:\步数变更.xlsx'

wb = load_workbook(filename=filename, read_only=True)




sheetName = "Sheet2"
ws = wb[sheetName]
rows=list(ws.rows)
print(rows)
# for row in ws.rows[1:]:
#     row_data = []
#     for cell in row:
#         row_data.append(cell.value)

# print(row_data)
