import csv
import json
import boto3
import io

def readcsv(file):
    csv_reader = csv.reader(io.StringIO(file))
    next(csv_reader)
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('TablaJuan')
    
    for row in csv_reader:
        item = {
            'id': row[0],
            'nombre': row[1],
            'apellido': row[2]
        }
        table.put_item(Item=item)
            
def lambda_handler(event, context):
    
    bucket = event['Records'][0]['s3']['bucket']['name']
    objeto = event['Records'][0]['s3']['object']['key']
    
    s3 = boto3.client('s3')
    
    response = s3.get_object(Bucket=bucket, Key=objeto)
    csvfile = response['Body'].read().decode('utf-8')
    
    readcsv(csvfile)
    
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }