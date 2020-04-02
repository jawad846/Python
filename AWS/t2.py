import boto3
session = boto3.Session(profile_name='expodev',region_name='eu-west-1')
aws_client = session.client('ec2')
response = aws_client.describe_instances()
print (response)
# for r in response['Reservations']:
#   for i in r['Instances']:
#     print (i['InstanceId'],i['InstanceType'],i['PrivateIpAddress'],i['ImageId'],i['LaunchTime'],i['Placement':'AvailabilityZone'])
    # for b in i['NetworkInterfaces']:
    #   print (b['PrivateIpAddress'], b['PublicIp']) 