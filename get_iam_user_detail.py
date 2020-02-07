import boto3
import datetime
import sys


session = boto3.session.Session(profile_name="adi_security")
iam_re = session.resource(service_name='iam')
# iam_re_user = iam_re.User("kaushik.pal@adidas-group.com")
# print(iam_re_user.name, iam_re_user.arn, iam_re_user.create_date, iam_re_user.user_name)
try:
    for each_iam in iam_re.users.all():
        print(each_iam.name, each_iam.arn, each_iam.create_time.strftime("%Y-%m-%d"))
except AttributeError as e:
    print(e)
    sys.exit(1)
except Exception as e:
    print(e)
    sys.exit(2)