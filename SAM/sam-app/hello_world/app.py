import json
import pandas

# import requests


def lambda_handler(event, context):
    
    #create dataframe in pandas
    df = pandas.DataFrame(columns=['name', 'age'])
    
    #return dataframe in json
    return {
        "statusCode": 200,
        "body": df.to_json(orient='records'),
    }
    
