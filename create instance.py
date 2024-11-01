import boto3
import os

# Initialize the EC2 resource
ec2 = boto3.resource('ec2')

# Environment variables that should be specified in Lambda
INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
KEY_NAME = os.environ['KEY_NAME']
AMI = os.environ['AMI']
SUBNET_ID = os.environ['SUBNET_ID']

def lambda_handler(event, context):   # Start of the Lambda handler function
    try:
        # Create EC2 instance
        instance = ec2.create_instances(
            InstanceType=INSTANCE_TYPE,  
            KeyName=KEY_NAME,            
            ImageId=AMI,                 
            SubnetId=SUBNET_ID,          
            MaxCount=1,
            MinCount=1,
            TagSpecifications=[{         # This creates a tag for the instance
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name', 'Value': 'systemvpc'}]
            }]
        )
        
        return {
            'statusCode': 200,
            'body': f"Instance created with ID: {instance[0].id}"
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': f"Failed to create instance: {str(e)}"
        }