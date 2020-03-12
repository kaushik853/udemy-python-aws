import boto3
import datetime
import sys


session = boto3.session.Session(profile_name="pyauto")
ec2_cli = session.client(service_name='ec2')
response = ec2_cli.describe_regions()
region_list = []
for reg in  response['Regions']:
     region_list.append(reg['RegionName'])


for i in region_list:
    ec2_cli = session.client(service_name='ec2', region_name=i)
    print(ec2_cli.describe_instances())