import boto3

s3 = boto3.client('s3')

s3.upload_file('index.html', 's3-demo-bucket-for-automation', 'index.html')
