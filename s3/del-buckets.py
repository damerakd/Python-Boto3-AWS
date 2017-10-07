#!/usr/bin/env python
import boto3
s3 = boto3.resource('s3')
for key in bucket.objects.all():
     key.delete()
bucket.delete  #Make Sure all keys in bucket are deleted Before the bucket is Deleted

