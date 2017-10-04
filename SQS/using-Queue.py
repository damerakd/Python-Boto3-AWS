#!/usr/bin/env python
import boto3
sqs = boto3.client('sqs');
response = sqs.list_queues()  #List all SQS Queues
response1 = sqs.create_queue(    #Creating a new Queue
    QueueName='xxxxx_NAME',
    Attributes ={
        'DelaySeconds': '60',
        'MessageRetentionPeriod' : '86400'
    }
)
