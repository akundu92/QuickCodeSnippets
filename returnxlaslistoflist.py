# Reading an excel file using Python and returing the entire dataset as list of list
import xlrd

#Converts excel date to python datetime as well
def convert_excel_to_tuple_list(fileloc,date_columns=(1,),datemode=0):
    # Give the location of the file



    # To open Workbook
    wb = xlrd.open_workbook(fileloc)
    sheet = wb.sheet_by_index(0)
    column_no=sheet.ncols
    row_no=sheet.nrows
    row_list=[]

    for i in range(row_no):
        t=[sheet.cell_value(i,j) for j in range(column_no)]
        if i>0:
            for k in date_columns:
                t[k]=xlrd.xldate_as_datetime(t[k],datemode)

        row_list.append(t)
    return row_list

print(convert_excel_to_tuple_list('sntestpy.xlsx'))

    #
    # # For row 0 and column 0
    # print(sheet.cell_value(0, 0))
    # print(sheet.cell_value(0, 1))
    # print(sheet.cell_value(0, 2))
    #
    # print(sheet.nrows)
    #
    # n=sheet.nrows
    #
    # for i in range(1,n):
    #     print(sheet.cell_value(i,0))
    #
    #     print(xlrd.xldate_as_datetime(sheet.cell_value(i, 1),0))
    #     print(type(xlrd.xldate_as_datetime(sheet.cell_value(i, 1),0)))
    #     print(sheet.cell_value(i, 2))
