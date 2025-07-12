import boto3
import os

def list_s3_files(bucket_name):
    """List all files in an S3 bucket."""
    s3 = boto3.client("s3")
    response = s3.list_objects_v2(Bucket=bucket_name)
    files = [obj['Key'] for obj in response.get('Contents', [])]
    print(f"Files in bucket: {files}")
    return files

def send_sns_message(topic_arn, message):
    """Send a message to an SNS topic."""
    sns = boto3.client("sns")
    sns.publish(TopicArn=topic_arn, Message=message)
    print(f"Sent message to topic {topic_arn}")

def handler(event, context):
    """Lambda entry point."""
    try:
        bucket_name = os.environ['BUCKET_NAME']
        topic_arn = os.environ['TOPIC_ARN']

        print("Starting Lambda execution.")
        files = list_s3_files(bucket_name)
        message = f"Lambda execution completed. Files in bucket: {files}"
        send_sns_message(topic_arn, message)

        print("Lambda completed successfully.")
        return {'statusCode': 200, 'body': 'Done'}

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return {'statusCode': 500, 'body': 'Error'}