import json
import datetime

# AWS SDK for Python
import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
s3_client = boto3.client('s3')


def lambda_handler(event, context):
    # Retrieve File Information

    try:
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        s3_file_name = event['Records'][0]['s3']['object']['key']
        print(bucket_name)
        print(s3_file_name)

    except KeyError:
        return {'statusCode': 404}

    print(bucket_name)
    print(s3_file_name)

    # Load Data in object
    json_object = s3_client.get_object(Bucket=bucket_name, Key=s3_file_name)
    json_file_reader = json_object['Body'].read()
    json_dict = json.loads(json_file_reader)

    print(json_dict)

    load_timestamp = datetime.datetime.now()
    dynamodb_table = dynamodb.Table(bucket_name)

    try:
        response = dynamodb_table.put_item(
            Item={
                'id': json_dict['id'],
                'price': json_dict['price'],
                'ticker': json_dict['ticker'],
                'load_timestamp': str(load_timestamp),
            }
        )
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': e.response['Error']['Message']
        }
    else:
        print("PutItem succeeded:")
        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }
