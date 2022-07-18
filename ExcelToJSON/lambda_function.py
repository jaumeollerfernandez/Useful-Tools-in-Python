import json
from readexcel import ReadExcel
from s3obtaindata import s3info
from exceltostring import ObtainExcelValues
from config import BUCKET,KEY,JSON
from introdict import IntroduceToJSON
from ExcelToJSON.readcsv import ReadCSV
from ExcelToJSON.obtainCSVvalues import obtainCSVvalues


def lambda_handler(event, context):
    
    #Obtenemos la lectura del objeto
    excelnoparsed = s3info(BUCKET,KEY)
    
    #Leemos la información en formato string
    values = obtainCSVvalues(excelnoparsed)
    
    #Obtenemos los valores en una lista.
    #values = ObtainExcelValues(excelparsed)
    
    #Transformamos a JSON
    jsontosend = IntroduceToJSON(values, BUCKET)
    
    #return values
    return jsontosend
    

