# coding: utf-8
import boto3
session = boto3.session.Session(profile_name='adi_security')
sts_client = session.client(service_name='sts')
sts_response = sts_client.get_caller_identity()
print(f"{sts_response['Account']} : {sts_response['Arn'].split(':')[-1]}" )