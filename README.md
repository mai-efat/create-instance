<h1 style="font-size: 36px;"></strong>Create an Amazon EC2 instance using lambda </strong></h1>

Below are the steps to set up a Lambda function that creates an EC2 instance:

# Setting Up a Lambda Function to Create an EC2 Instance

Below are the steps to set up a Lambda function that creates an EC2 instance:

## Steps

1. **Create an IAM Role**
   - Create an IAM role with the policy `AmazonEC2FullAccess` for Lambda.

2. **Create a Lambda Function**
   - Go to the AWS Lambda console and click on **Create function**.

3. **Select the Runtime**
   - Choose the runtime as **Python 3.x**.
   - Under **Permissions**, choose the existing role you created earlier (e.g., `LambdaEC2Role`).

4. **Write the Lambda Function Code**
   - Implement the code to create the EC2 instance.

5. **Configure Environment Variables (if needed)**
   - Set the AMI ID, key pair name, security group ID, and subnet ID as environment variables to avoid hardcoding them.

6. **Test the Lambda Function**
   - Create a test event and execute the function to ensure it works as expected.

## Note on Environment Variables

Using environment variables for sensitive data such as the AMI ID, key pair name, security group ID, and subnet ID is recommended. This approach enhances security and flexibility, allowing you to change these values without modifying the function code.




 
 
 Environment Variables:  the AMI ID, key pair name, security group ID, and subnet ID to avoid hardcoding them.
