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
    headers = get_headers(event)
    if method == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                "Access-Control-Allow-Origin": '*',
                'Access-Control-Allow-Headers': '*'
            },
        }

    url = get_path(event)

    #
    # Need to extract Cookie as XCookie because browser refuses to pass Cookie
    #
    headers['Cookie'] = headers['xcookie']
    del headers['xcookie']

    response = requests.get(url, headers=headers)

    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Origin": '*',
            'Access-Control-Allow-Headers': '*'
        },
        'body': response.text
    }

