''' Role for Lambda--> To get access of any aws required EC2 service through 
Create Lambda function code, assign the above Role
Schedule a cloudwatch trigger with Rules and Cron job 0 8 am ? * MON-FRI * to start ec2
Another lambda to stop ec2 at 5 pm everyday with cloudwatch trigger rule
'''

import boto3
def lambda_handler(event, context):
    ec2_con = boto3.resource(service_name="ec2", region_name="eu-central-1")
    test_env_filter = {"Name":"tag:Env", "Values":["Test"]}
    for each_ in ec2_con.instances.filter(Filters=[test_env_filter]):
        each_.start()

#ec2 resource object
#my_ins = ec2_con.Instance('INSTANCE-ID')
#For SNS topic
#sns_client.publish(TargetArn='SNS-TOPIC-ARN', Message=my_ins.state['Name'])