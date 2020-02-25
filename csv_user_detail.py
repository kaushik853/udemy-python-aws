import boto3
import csv
from datetime import datetime
import sys
from pprint import pprint

session = boto3.session.Session(profile_name="adi_security")
# iam_cli = session.client(service_name='iam')
# # iam_re_user = iam_re.User("kaushik.pal@adidas-group.com")
# # print(iam_re_user.name, iam_re_user.arn, iam_re_user.create_date, iam_re_user.user_name)
# for each_ in iam_cli.list_users()['Users']:
#     print(each_['UserName'], each_['UserId'], each_['CreateDate'])
#     pprint(iam_cli.list_groups_for_user(UserName=each_['UserName']))

#list1 = []
iam_re = session.resource(service_name='iam')
# iam_re_user = iam_re.User("kaushik.pal@adidas-group.com")
# print(iam_re_user.name, iam_re_user.arn, iam_re_user.create_date, iam_re_user.user_name)
#try:
csv_ob=open("test_user_info.csv","w",newline='')
csv_w=csv.writer(csv_ob)
csv_w.writerow(["IAM-User","User-Id",'User-ARN', "User-Create-Date", "User-Group", "Policy-Name"])
for each_iam in iam_re.users.all():
    data = (each_iam.name, each_iam.user_id, each_iam.arn, each_iam.create_date.strftime("%Y-%m-%d"), )
    #print(data)
    for i in iam_re.meta.client.list_groups_for_user(UserName=each_iam.name)['Groups']:
        #print(i['GroupName'])
        data = data + (i['GroupName'],)
       # print(iam_re.meta.client.list_attached_group_policies(GroupName=i['GroupName'])
        for j in iam_re.meta.client.list_attached_group_policies(GroupName=i['GroupName'])['AttachedPolicies']:
            data = data + (j['PolicyName'],)
    csv_w.writerow([data[0], data[1], data[2], data[3], data[4], data[5]])

csv_ob.close()










