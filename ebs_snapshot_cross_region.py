import os, sys
try:
    import boto3
    print("Imported boto3 successfully")
except Exception as e:
    print(e)
    sys.exit(1)
source_region = 'us-east-1'
dest_region = 'us-east-2'

session = boto3.session.Session(profile_name='adi_security')
ec2_source_client = session.client(service_name='ec2', region_name=source_region)
sts_client = session.client(service_name='sts', region_name=source_region)
account_id = sts_client.get_caller_identity().get('Account')
bkp_snap = []
filter_bkp = {'Name':'tag:backup','Values':['Yes']}
for each_ in ec2_source_client.describe_snapshots(OwnerIds=[account_id],Filters=[filter_bkp]).get('Snapshots'):
    bkp_snap.append(each_.get('SnapshotId'))

ec2_dest_client = session.client(service_name='ec2', region_name=dest_region)
for each_ in bkp_snap:
    print(f"taking backup for id of {each_} into a {dest_region}")
    ec2_dest_client.copy_snapshot(
        Description='Disaster Recovery',
        SourceRegion=source_region,
        SourceSnapshotId=each_
    )
   waiter = ec2_dest_client.get_waiter('snapshot_completed')
   waiter.wait(SnapshotIds=[each_])
    #define a waiter function for completion of snapshots
print("ebs snapshot copy to destination region is completed")
print("Modifying the snapshot tags for which backup is completed")
for each_ in bkp_snap:
    ec2_source_client.delete_tags(
        Resources=[each_],
        Tags=[
        {
        'Key':'backup'
        'value':'yes'
        }
        ]
    )
    ec2_source_client.create_tags(
        Resources=[each_],
        Tags=[
        {
        'Key':'backup'
        'value':'completed'
        }
        ]
    )