# coding: utf-8
import boto3
session = boto3.session.Session(profile_name='adi_security')
ec2_client = session.client(service_name='ec2')
ec2_client_reserv = ec2_client.describe_instances()['Reservations']
for ec2 in ec2_client_reserv:
    for i in ec2['Instances']:
        print(f"this is: {i['InstanceId']}\nThis Launch time: {i['LaunchTime']}")


ec2_client_volume = ec2_client.describe_volumes()['Volumes']
for ec2_vol in ec2_client_volume:
    print(f"The Volune id is: {ec2_vol['VolumeId']}\nThe availability zone is: {ec2_vol['AvailabilityZone']}\nThe state is: {ec2_vol['State']}")