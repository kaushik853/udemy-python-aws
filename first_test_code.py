import boto3
session = boto3.session.Session(profile_name='adi_security')
iam_resource = session.resource('iam')
iam_client = session.client('iam')
#we can user 'service_name' and 'region_name' also as part of creating resource or client variable
iam_users = iam_resource.users.all()
for user in iam_users:
    print(user.name)

iam_cli_users = iam_client.list_users()
for user in iam_cli_users['Users']:
    print(user['UserName'])
