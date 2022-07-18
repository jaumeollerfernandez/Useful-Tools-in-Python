import json
import boto3
import os
import config

def IntroduceToJSON(pMatrix, pBucket):
    matrix = pMatrix
    dicto = {}
    bucket = pBucket
    
    for i in range(len(matrix)):
        aux = {
            "name":"",
            "ID":"",
            "department":"",
            "value": ""
        }
        for j in range(len(matrix[0])):
            aux["name"] = matrix[i][1]
            aux["ID"] = matrix[i][2]
            aux["department"] = matrix[i][3]
            aux["value"] = matrix[i][0]
            dicto[f"{i}"] = aux
            
    fp = open("/tmp/jsonDict.js", "w+")
    fp.write("var jsonDict = ")
    fp.write(str(dicto))
    fp.close()
    
    fp = open("/tmp/jsonDict.js","r")
    print(fp.read())
    fp.close()
    s3 = boto3.resource('s3')
    s3.Object(bucket, 'jsonDict.js').delete()
    s3.Bucket(bucket).upload_file('/tmp/jsonDict.js','jsonDict.js')  
        
    #print(os.path.isfile("/tmp/jsonDict.js"))
    #print(type(dicto))
    return dicto