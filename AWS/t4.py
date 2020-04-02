import boto3
session = boto3.Session(profile_name='expodev',region_name='eu-west-1')
ec2_describe = boto3.resource('ec2')
    instance = ec2_describe.instances.filter(
        Filters = [ {
            'Name' : 'instance-state-name',
            'Values' : [ 'running' ]
        } ]
    )
for i in instances:
    print(i.instance-id)
    print(i.image-id)