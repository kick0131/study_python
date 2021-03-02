import pprint


def lambda_handler(event, context):
    print(f'--- {__name__} ---')
    pprint.pprint(event)

    return {
        "statusCode": 200,
        "body": 'hello'
    }
