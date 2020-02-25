#!/bin/python                                                                                                             
import boto3                                                                                                              
from random import choice                                                                                                 
import sys 
import click



# def hello(username, cliaccess, consoleaccess, policyarn):
#     click.echo(f"this user {username} need CliAccess {cliaccess} ConsoleAccess {consoleaccess} and the PolicyARN is arn:aws:iam::aws:policy/{policyarn}")



def get_iam_client_object():                                                                                              
    session=boto3.session.Session(profile_name="adi_security")                                                                
    iam_client=session.client(service_name="iam",region_name="eu-central-1")                                                 
    return iam_client  


def get_random_password():
    len_of_pass = 11
    valid_pass_option = "QWERTYUIOPASDFGHJKLZXCVBNMqazwsxedcrfvtgbyhnujmikolp0123456789!@#$%^&*()?"
    password = []
    for i in range(len_of_pass):
        password.append(choice(valid_pass_option))
    random_pass = "".join(password)
    return random_pass



@click.command()
@click.option("--username", prompt="IAM-UserName", help="iam username to be created")
@click.option("--cliaccess", prompt="cli access answer in Yes or No", help="cli access is needed for user")
@click.option("--consoleaccess", prompt="console access answer in Yes or No", help="console access is needed for user")
@click.option("--policyarn", prompt="policyarn", help="mention the policy arn user needs")

def create_user(username, cliaccess, consoleaccess, policyarn):
    iam_client = get_iam_client_object()
    iam_user_name = username
    passwrd = get_random_password()
    PolicyArn = 'arn:aws:iam::aws:policy/'+ policyarn
    try:
        iam_client.create_user(UserName=iam_user_name)
    except Exceptionas as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            click.echo(f"There is already a username with {iam_user_name}")
            sys.exit(0)
        else:
            print("Verify the following error and retry")
            print(e)
            sys.exit(1)
    
    
    if cliaccess=="Yes" or cliaccess=="yes" or cliaccess=="YES":
        response = iam_client.create_access_key(UserName=iam_user_name)
        click.echo(f"IAM User Name={iam_user_name}")                                                                        
        click.echo(f"AccessKeyId={response['AccessKey']['AccessKeyId']}\nSecretAccessKey={response['AccessKey']['SecretAccessKey']}")
    

    if cliaccess=="No" or cliaccess=="no" or cliaccess=="NO":
        click.echo(f"The user {iam_user_name} does not need cli access")
    
    if consoleaccess=="Yes" or consoleaccess=="yes" or consoleaccess=="YES":
        iam_client.create_login_profile(UserName=iam_user_name, Password=passwrd, PasswordResetRequired=False)
        click.echo(f"The user {iam_user_name} has password {passwrd}")
    

    if consoleaccess=="No" or consoleaccess=="no" or consoleaccess=="NO":
        click.echo(f"The user {iam_user_name} does not need console access")


    
    iam_client.attach_user_policy(UserName=iam_user_name, PolicyArn=PolicyArn)
    return None


if __name__=="__main__":
    create_user()