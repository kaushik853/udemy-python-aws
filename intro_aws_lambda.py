import boto3
def lambda_handler(event, context):
    ec2_con = boto3.resource(service_name="ec2", region_name="eu-central-1")
    for each_ in ec2_con.instances.all():
        print(each_.id)

LambdaRole = Ec2ReadOnly