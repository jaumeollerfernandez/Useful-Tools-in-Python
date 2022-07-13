import boto3

def s3info(pBucket, pKey):
    
    s3 = boto3.client('s3')
    bucket = pBucket
    key = pKey
    
    data = s3.get_object(Bucket=bucket, Key= key)
    response = data['Body'].read() 
    
    return response