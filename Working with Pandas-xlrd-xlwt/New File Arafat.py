import xlrd
import xlwt

ExcelFileName = "F:\ALL\F drive All\ACM GROUP\Phyton\T_Daily_Min(Bari).xlsx"

workbook = xlrd.open_workbook(ExcelFileName)
worksheet = workbook.sheet_by_index(0)
workssheetname = workbook.sheet_names()

book = xlwt.Workbook()
name = []
for n in workssheetname:
    s = workbook.sheet_by_name(n)
    name.append(str(s))
    print(s)
w = 0
for s in workbook.sheets():

    data = name[w]
    w = w + 1
    #sheet = book.add_sheet(str(data))

    num_rows = s.nrows
    num_cols = s.ncols

    i = 0
    j = 0
    k = 0
   # for curr_row in range(1, num_rows):

      #  for curr_col in range(2, num_cols):

          #  try : data = s.cell_value(curr_row, curr_col)  # Read the data in the current cell
         #   except : continue
            # print(data)
         #   if data == "":
        #        continue

           # sheet.write(i, j, data)

           # i = i + 1

      #  k = k + 1

       # if k == 12:
       #     i = 0
       #     j = j + 1
       #     k = 0



book.save('O_NEW.xls')

