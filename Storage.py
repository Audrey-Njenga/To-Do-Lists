# this is the class that helps to read and write from the csv file
# that is being used as the storage fot this app
import xlrd
from openpyxl import workbook, load_workbook


class Csv:
    def __init__(self):
        self = self

    def read_data(self):
        loc = "project_storage.xlsx"
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        data = (sheet.cell_value(0, 0))
        return data

    def store(self, data):
        loc = "project_storage.xlsx"
        wb = load_workbook(loc)
        sheet = wb.get_sheet_by_name("Sheet1")
        sheet['A1'] = data
        wb.save(loc)


storage_object = Csv()

