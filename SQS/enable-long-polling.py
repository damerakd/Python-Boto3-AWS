#!/usr/bin/env python
import boto3

sqs = boto3.client('sqs')

queue_url = 'xxxxx'  #your sqs queue url

# Enable long polling on an existing SQS queue
sqs.set_queue_attributes(
    QueueUrl=queue_url,
    Attributes={'ReceiveMessageWaitTimeSeconds': '20'}
)
