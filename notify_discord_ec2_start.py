import boto3
import requests
import time

def lambda_handler(event, context):
    instance_id = event['detail']['instance-id']
    ec2 = boto3.client('ec2')

    # IPが付くまで待つ
    public_ip = None
    for _ in range(10):
        instance = ec2.describe_instances(InstanceIds=[instance_id])
        public_ip = instance['Reservations'][0]['Instances'][0].get('PublicIpAddress')
        if public_ip:
            break
        time.sleep(3)

    webhook_url = "your web hook"

    payload = {
        "content": f"your message.\nIPアドレス:\n```{public_ip}```"
    }

    response = requests.post(webhook_url, json=payload)

    print("status:", response.status_code)
    print("response:", response.text)

    response.raise_for_status()

    return "Discord notified."
