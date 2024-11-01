import boto3
import os

ec2_client = boto3.client('ec2')

def lambda_handler(event, context):
    # Specify your instance ID
    instance_id = os.environ['INSTANCE_ID']
    
    # Start the instance
    print(f"Starting EC2 instance {instance_id}")
    ec2_client.start_instances(InstanceIds=[instance_id])
    
    return {
        'statusCode': 200,
        'body': f"EC2 instance {instance_id} started."
    }
