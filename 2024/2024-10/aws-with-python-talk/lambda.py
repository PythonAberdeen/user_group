import boto3
import json
import time
from botocore.exceptions import ClientError

# Initialize the Lambda client
lambda_client = boto3.client('lambda', region_name='eu-west-2')  # London region

# Define parameters
function_name = 'my_lambda_function'
role_arn = 'arn:aws:iam::311708042980:role/my_lambda_execution_role'  # Replace with your IAM role ARN
handler = 'lambda_function.lambda_handler'  # The function handler in your code
runtime = 'python3.9'  # Python runtime version
zip_file_path = 'lambda_function.zip'  # Path to your zip file containing the Lambda function code

# Sample Lambda function code
lambda_code = """
import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
"""

# Step 1: Create a Lambda function
def create_lambda_function():
    try:
        # Create a directory to hold the lambda function code
        with open('lambda_function.py', 'w') as f:
            f.write(lambda_code)

        # Create the ZIP file with the lambda function code
        import zipfile
        with zipfile.ZipFile(zip_file_path, 'w') as zipf:
            zipf.write('lambda_function.py')

        with open(zip_file_path, 'rb') as f:
            zipped_code = f.read()
        
        response = lambda_client.create_function(
            FunctionName=function_name,
            Runtime=runtime,
            Role=role_arn,
            Handler=handler,
            Code=dict(ZipFile=zipped_code),
            Description='A simple Lambda function',
            Timeout=10,
            MemorySize=128,
            Publish=True,
        )
        print(f"Lambda function '{function_name}' created successfully.")
    except ClientError as e:
        print(f"Error creating Lambda function: {e}")

# Step 2: Invoke the Lambda function
def invoke_lambda_function():
    try:
        response = lambda_client.invoke(
            FunctionName=function_name,
            InvocationType='RequestResponse'
        )
        payload = json.loads(response['Payload'].read())
        print("Lambda function response:", payload)
    except ClientError as e:
        print(f"Error invoking Lambda function: {e}")

# Step 3: Get details of the Lambda function
def get_lambda_function_details():
    try:
        response = lambda_client.get_function(FunctionName=function_name)
        print("Lambda function details:", response)
    except ClientError as e:
        print(f"Error getting Lambda function details: {e}")

# Step 4: Delete the Lambda function
def delete_lambda_function():
    try:
        lambda_client.delete_function(FunctionName=function_name)
        print(f"Lambda function '{function_name}' deleted successfully.")
    except ClientError as e:
        print(f"Error deleting Lambda function: {e}")

# Execute the steps
create_lambda_function()
time.sleep(5)  # Wait a moment to ensure the function is created
invoke_lambda_function()
get_lambda_function_details()
delete_lambda_function()
