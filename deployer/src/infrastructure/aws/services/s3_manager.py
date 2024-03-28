import logging
import boto3
from botocore.exceptions import ClientError

def create_bucket(bucket_name, region=None):

def delete_bucket(bucket_name, region=None):

if __name__=="__main__":
    create_bucket("remote-tfstate-us-east-1")
    delete_bucket("remote-tfstate-us-east-1")
