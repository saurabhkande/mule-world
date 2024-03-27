def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello, here is Lambda deployed using SAM template'
    }