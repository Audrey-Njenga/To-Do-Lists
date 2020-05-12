# this is the class that helps to read and write from the csv file
# that is being used as the storage fot this app
import xlrd


class Csv:
    def __init__(self):
        self = self

    def read_data(self):
        loc = "ProjectStorage.xlsx"

        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        print(sheet.cell_value(0, 0))

    # def store(self, data):


storage_object = Csv()
storage_object.read_data()
