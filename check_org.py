import boto3
from pprint import pprint


session = boto3.session.Session(profile_name="adi_security")
org_cli = session.client(service_name='organizations')
response = org_cli.describe_organization()
print(f" {response['Organization']['MasterAccountArn']}\n {response['Organization']['MasterAccountEmail']} \n {response['Organization']['MasterAccountId']}" )