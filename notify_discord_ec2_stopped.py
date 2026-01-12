import boto3
import requests
import time

def lambda_handler(event, context):
    instance_id = event['detail']['instance-id']
    ec2 = boto3.client('ec2')

    public_ip = None

    try:
        instance = ec2.describe_instances(InstanceIds=[instance_id])
        public_ip = instance['Reservations'][0]['Instances'][0].get('PublicIpAddress')
    except Exception as e:
        print("IP取得失敗:", e)

    if public_ip:
        message = f"your message.\nIPアドレス: ```{public_ip}```"
    else:
        message = "your message.\nIPアドレス: 取得できませんでした。"

    webhook_url = "your web hook"
    data = {
        "content": message
    }

    response = requests.post(webhook_url, json=data)
    print("status:", response.status_code)
    print("body:", response.text)

    response.raise_for_status()
