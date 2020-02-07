import boto3
import datetime
import sys


session = boto3.session.Session(profile_name="adi_security")
iam_re = session.resource(service_name='iam')
for each_policy in iam_re.policies.all():
    print(each_policy)