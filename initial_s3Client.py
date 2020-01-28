import boto3
session = boto3.session.Session(profile_name='adi_security')
s3_client = session.client(service_name='s3')
s3_client_response = s3_client.list_buckets()
for each in s3_client_response['Buckets']:
    print(each['Name'])