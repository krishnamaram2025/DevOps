import boto3    
s3 = boto3.resource('s3')
bucket = s3.Bucket('remote-tfstate-us-east-1')
bucket.delete()
