#!/usr/bin/env python
import boto3
sqs = boto3.client('sqs')
response = sqs.get_queue_url(QueueName='xxxxx_NAME') #Retrieve Url for SQS Queue
print(response['QueueUrl'])
sqs.delete_queue(QueueUrl='SQS_QUEUE_URL')  #Delete a Particular Queue by Queue Name
