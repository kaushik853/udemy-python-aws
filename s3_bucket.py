import boto3

session = boto3.session.Session(profile_name='adi_security')
s3_re = session.resource(service_name='s3', region_name='us-east-1')

for each_bucket in s3_re.buckets.all():
    print(each_bucket.name)


s3_cli = session.client(service_name='s3', region_name='us-east-1')
for each_ in s3_cli.list_buckets().get('Buckets'):
    print(each_.get('Name'))

#Use paginator to get bucket object list if they are more than 1000
bucket_name = "test_bucket"
bucket_object = s3_re.Bucket(bucket_name)
for each_obj in bucket_object.objects.all():
    print(each_obj.key)


bucket_obj_cli = s3_cli.list_objects(Bucket=bucket_object)
for buck_obj in bucket_obj_cli['Contents']:
    print(buck_obj.get('Key'))


paginator = s3_cli.get_paginator('list_objects')
for each_page in paginator.paginate(Bucket=bucket_name):
    for each_obj in each_page['Contents']:
        print(each_obj['Key'])


