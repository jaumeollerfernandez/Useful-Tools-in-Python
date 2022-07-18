import pandas as pd
import openpyxl

def ReadCSV(pExcel):
    lecture = str(pd.read_csv(pExcel))
    return lecture
