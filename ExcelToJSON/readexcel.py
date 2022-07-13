import pandas as pd
import openpyxl

def ReadExcel(pExcel):
    lecture = str(pd.read_excel(pExcel))
    return lecture