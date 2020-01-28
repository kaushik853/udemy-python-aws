# coding: utf-8
import boto3
session1 = boto3.session.Session(profile_name='adi_security')
adi_s3 = session1.resource('s3')
adi_buckets = adi_s3.buckets.all()
for bucket in adi_buckets:
    print(bucket.name)

""" cf-templates-l0zq151becb5-eu-central-1
config-bucket-567796756587
ct-all-s-south
test-adi-redirect """
    
session2 = boto3.session.Session(profile_name='pyauto')
priv_s3 = session2.resource('s3')
priv_buckets = priv_s3.buckets.all()
for bucket in priv_buckets:
    print(bucket.name)

""" 
kaushikvideoanalyzervideos
kaushikvideolyzervideos12345
notifon-notifier-dev-serverlessdeploymentbucket-kh0d4r4rlrcq
rekognition-video-console-demo-fra-389938739438-67riszsb8vzvbo
tarabirthday-de
tarabirthday-logs
videolyzer-dev-serverlessdeploymentbucket-7ge103zt4t5u """
    
