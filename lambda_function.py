import json

import requests


def get_path(event):
    path = event['rawPath'] # e.g. /foo/bar/biz/baz
    stripped_path = path[1:] # strip off leading slash
    return stripped_path


def get_method(event):
    method = event['requestContext']['http']['method']
    return method


def get_headers(event):
    headers = event['headers']
    return headers



def lambda_handler(event, context):
    method = get_method(event)
    if method == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type"
            },
        }

    headers = get_headers(event)
    url = get_path(event)
    response = requests.get(url, headers=headers)

    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type"
        },
        'body': response.text
    }

