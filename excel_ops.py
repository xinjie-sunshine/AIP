import xlrd
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
Path = os.path.split(curPath)[0]
sys.path.append(Path)

class ExcelUtil():
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # Get the first row as the key value
        self.keys = self.table.row_values(0)
        # Get the total number of rows
        self.rowNum = self.table.nrows
        # Get the total number of columns
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum-1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r

    def get_main_title(self):
        values = self.table.cell(1,0).value
        return values

    def get_pic_delete(self):
        values = self.table.cell(1,1).value
        return values


if __name__ == "__main__":
    filepath = "AIP.xlsx"
    sheetName = "pic_reporter_prefix"    
    data = ExcelUtil(filepath, sheetName)
    print(data.get_main_title())
    print(data.get_pic_delete())