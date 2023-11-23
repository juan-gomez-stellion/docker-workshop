import csv
import json

def readcsv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
            
def lambda_handler(event, context):
    
    bucket = event['Records'][0]['s3']['bucket']['name']
    objeto = event['Records'][0]['s3']['object']['key']
    
    print(bucket)
    print(objeto)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }