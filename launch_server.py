import boto3

def lambda_handler(event, context):
    instance_id = 'your id'
    ec2 = boto3.client('ec2')

    instance = ec2.describe_instances(InstanceIds=[instance_id])
    state = instance['Reservations'][0]['Instances'][0]['State']['Name']

    if state in ['running', 'pending']:
        return f"Instance already {state}."

    ec2.start_instances(InstanceIds=[instance_id])

    return "your text in the web."