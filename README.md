<h1 style="font-size: 36px;"></strong>Create an Amazon EC2 instance using lambda </strong></h1>

Below are the steps to set up a Lambda function that creates an EC2 instance:
'''
 Step 1: Create an IAM Role AmazonEC2FullAccess  for Lambda
 Step 2: Create a Lambda Function
 Step 3:Select the runtime as Python 3.x.
 Under Permissions, choose the existing role you created earlier (e.g., LambdaEC2Role).
 Step 4: Write the Lambda Function Code
 Step 5: Configure Environment Variables (if needed)
 Step 6: Test the Lambda Function
 '''




 
 
 Environment Variables:  the AMI ID, key pair name, security group ID, and subnet ID to avoid hardcoding them.
