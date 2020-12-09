
import xlsxwriter
import numpy as np

B = []

for i in range(1000):
    xr = np.random.permutation([1 ,2 ,3 , 4])
    B.append(xr)
print(B)

with xlsxwriter.Workbook('C:/Users/sarina/Desktop/perm.xlsx') as workbook:
    worksheet = workbook.add_worksheet()

    for row_num, data in enumerate(B):
        worksheet.write_row(row_num, 0, data)

