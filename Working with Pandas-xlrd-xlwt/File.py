import xlrd
import xlwt

ExcelFileName = "F:\ALL\F drive All\ACM GROUP\Phyton\Daily_Total_Rainfall_Bari.xlsx"

workbook = xlrd.open_workbook(ExcelFileName)
worksheet = workbook.sheet_by_index(0)

book = xlwt.Workbook()

for s in workbook.sheets():

    data = s.cell_value(2, 0)
    sheet = book.add_sheet(str(data))
    sheet.write(0, 0, str(data))

    num_rows = s.nrows
    num_cols = s.ncols

    i = 1

    for curr_row in range(1, num_rows):

        for curr_col in range(3, num_cols):

            try : data = s.cell_value(curr_row, curr_col)  # Read the data in the current cell
            except : pass
            # print(data)
            sheet.write(i, 0, data)
            i = i + 1

book.save('Data.xls')

