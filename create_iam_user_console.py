import boto3
from random import choice
import sys


def get_iam_client_object():
    session = boto3.session.Session(profile_name='adi_security')
    iam_client = session.client(service_name='iam', region_name='eu-central-1')
    return iam_client


def get_random_password():
    len_of_pass = 11
    valid_pass_option = "QWERTYUIOPASDFGHJKLZXCVBNMqazwsxedcrfvtgbyhnujmikolp0123456789!@#$%^&*()?"
    password = []
    for i in range(len_of_pass):
        password.append(choice(valid_pass_option))
    random_pass = "".join(password)
    return random_pass


def create_user():
    iam_client = get_iam_client_object()
    iam_user_name = 'doitwithpython@gmail.com'
    passwrd = get_random_password()
    PolicyArn = 'arn:aws:iam::aws:policy/AdministratorAccess'
    try:
        iam_client.create_user(UserName=iam_user_name)
    except Exceptionas as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print(f"There is already a username with {iam_user_name}")
            sys.exit(0)
        else:
            print("Verify the following error and retry")
            print(e)
            sys.exit(1)
    iam_client.create_login_profile(UserName=iam_user_name, Password=passwrd, PasswordResetRequired=False)
    iam_client.attach_user_policy(UserName=iam_user_name, PolicyArn=PolicyArn)
    print(f"The user {iam_user_name} has password {passwrd}")
    return None


if __name__=="__main__":
    create_user()