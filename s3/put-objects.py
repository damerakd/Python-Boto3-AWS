#!/usr/bin/env python
import boto3
s3 = boto3.resource('s3')
s3.Bucket('various-certifications').put_object(Key='sample.txt')
