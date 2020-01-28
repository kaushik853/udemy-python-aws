import boto3
import csv
from pprint import pprint
from datetime import datetime
aws_mag_con=boto3.session.Session(profile_name="adi_security")
# ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")
# cnt=1
# csv_ob=open("inventory_info.csv","w",newline='')
# csv_w=csv.writer(csv_ob)
# csv_w.writerow(["S_NO","Instance_Id",'Instance_Type','Architecture','LaunchTime','Privat_Ip'])
# for each in ec2_con_re.instances.all():
# 	print(cnt,each,each.instance_id,each.instance_type,each.architecture,each.launch_time.strftime("%Y-%m-%d"),each.private_ip_address)
# 	csv_w.writerow([cnt,each.instance_id,each.instance_type,each.architecture,each.launch_time.strftime("%Y-%m-%d"),each.private_ip_address])

# 	cnt+=1
# csv_ob.close()

# with client variable
ec2_client = aws_mag_con.client(service_name="ec2")
cnt=1
csv_ob=open("inventory_info.csv","w",newline='')
csv_w=csv.writer(csv_ob)
csv_w.writerow(["S_NO","Instance_Id",'Instance_Type','Architecture','LaunchTime','Privat_Ip'])
ins1 = ['i-01666983d85d15a5c', 'i-02ed212218a99067a']
ins = ec2_client.describe_instances()
for each in ins['Reservations']:
	#csv_w.writerow([each['Instances']['InstanceId'], each['Instances']['InstnaceType'], each['Instance']['Architecture'], each['Instances']['LaunchTime'].strftime("%Y-%m-%/d"), each['Instances']['NetworkInterfaces']['PrivateIpAddress']])
	for each_int in each['Instances']:
		csv_w.writerow([cnt, each_int['InstanceId'], each_int['InstanceType'], each_int['Architecture'], each_int['LaunchTime'].strftime('%Y-%m-%d'), each_int['PrivateIpAddress']])
		#print(each_int['InstanceId'], each_int['InstanceType'], each_int['Architecture'], each_int['LaunchTime'].strftime('%Y-%m-%d'), each_int['PrivateIpAddress'])
		cnt+=1

csv_ob.close()