import json
import boto3
import base64

def add_numbers(event, context):
    """
    Lambda function to add two numbers
    """
    try:
        num1 = event.get('num1', 0)
        num2 = event.get('num2', 0)
        result = num1 + num2
        
        return {
            'statusCode': 200,
            'body': json.dumps({'result': result})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def upload_to_s3(event, context):
    """
    Lambda function to upload document to S3
    """
    s3_client = boto3.client('s3')
    
    try:
        # Assumes document is base64 encoded in the event
        file_content = base64.b64decode(event['document'])
        file_name = event.get('filename', 'document.pdf')
        bucket_name = 'static-bucket'
        
        s3_client.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=file_content
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'File uploaded successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }