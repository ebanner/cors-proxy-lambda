import json


def lambda_handler(event, context):
    method = event['requestContext']['http']['method']
    if method == 'OPTIONS':
        return {
            'statusCode': 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type"
            },
        }


    return {
        'statusCode': 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type"
        },
        'body': json.dumps('Hello from Lambda!')
    }

