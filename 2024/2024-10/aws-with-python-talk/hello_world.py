import boto3

# Create an STS client using Boto3
sts_client = boto3.client('sts')

# Call the get_caller_identity() API to verify credentials
response = sts_client.get_caller_identity()

# Print out the details of the authenticated AWS account
print("Hello, World! You are authenticated with the following details:")
print(f"AWS Account ID: {response['Account']}")
print(f"User ARN: {response['Arn']}")
print(f"User ID: {response['UserId']}")
