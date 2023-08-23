import boto3

def get_messages_from_queue(queue_url):
    sqs = boto3.client('sqs', region_name='us-west-2', endpoint_url='http://localhost:4566')
    messages = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=10)
    return messages.get('Messages', [])
