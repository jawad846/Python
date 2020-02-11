import boto3
session = boto3.Session(profile_name='expodev',region_name='eu-west-1')
def list_instances_by_tag_value(tagkey, tagvalue):
    # When passed a tag key, tag value this will return a list of InstanceIds that were found.

    aws_client = session.client('ec2')

    response = aws_clien.describe_instances(
        Filters=[
            {
                'Name': 'tag:'+tagkey,
                'Values': [tagvalue]
            }
        ]
    )
    instancelist = []
    for reservation in (response["Reservations"]):
        for instance in reservation["Instances"]:
            instancelist.append(instance["InstanceId"])
    return instancelist