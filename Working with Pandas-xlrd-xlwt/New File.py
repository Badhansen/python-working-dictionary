import xlrd
import xlwt

ExcelFileName = "F:\ALL\F drive All\ACM GROUP\Phyton\\NewProject\\New data file.xlsx"

workbook = xlrd.open_workbook(ExcelFileName)
worksheet = workbook.sheet_by_index(0)

book = xlwt.Workbook()

for s in workbook.sheets():

    data = s.cell_value( 1, 0 )
    sheet = book.add_sheet( str( data ) )
    sheet.write( 0, 0, str( data ) )
    num_rows = s.nrows
    num_cols = s.ncols

    i = 1
    j = 0
    for curr_row in range( 1, num_rows ):

        for curr_col in range( 3, num_cols ):

            try : data = s.cell_value( curr_row, curr_col )  # Read the data in the current cell
            except : pass

            if data == "":
                continue

            sheet.write( i, j, data )

            i = i + 1

book.save('Single column list.xls')