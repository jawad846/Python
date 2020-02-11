import boto3
session = boto3.Session(profile_name='expodev',region_name='eu-west-1')
dev_client = session.client('rds')
response = dev_client.describe_db_instances('DBInstanceIdentifier')
print(response)