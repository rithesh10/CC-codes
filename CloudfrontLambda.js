import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('FeedbackTable')

def lambda_handler(event, context):
    body = json.loads(event['body'])

    item = {
       
        'rollno': body['rollno'],       # ✅ matching frontend lowercase key
        'name': body['name'],
        'subject': body['subject'],
        'rating': body['rating']
    }

    table.put_item(Item=item)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',  # or your frontend domain
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'POST,OPTIONS'
        },
        'body': json.dumps({ 'message': 'Feedback received!' })
    }
