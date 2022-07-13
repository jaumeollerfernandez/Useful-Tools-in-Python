import json
from readexcel import ReadExcel
from s3obtaindata import s3info
from exceltostring import ObtainExcelValues

def lambda_handler(event, context):
    
    futurejson = {}
    #Nombre del Bucket
    bucket = 'bucket-name'
    
    #Nombre del excel
    key = 'key-name'
    
    #Obtenemos la lectura del objeto
    excelnoparsed = s3info(bucket,key)
    
    #Leemos la información en formato string
    excelparsed = ReadExcel(excelnoparsed)
    
    #Obtenemos los valores en una lista.
    values = ObtainExcelValues(excelparsed)
    
    
    return values
    

