import boto3
import time
from botocore.exceptions import ClientError

# Initialize the EC2 client for the London region
ec2_client = boto3.client('ec2', region_name='eu-west-2')  # London region

# Define parameters
instance_type = 't2.micro'  # Instance type
ami_id = 'ami-0b45ae66668865cd6'  # Replace with a valid AMI ID for the London region
key_name = 'my-key-pair'  # Replace with your EC2 Key Pair name

# Step 1: Launch an EC2 instance
try:
    print("Launching EC2 instance...")
    response = ec2_client.run_instances(
        InstanceType=instance_type,
        ImageId=ami_id,
        KeyName=key_name,
        MinCount=1,
        MaxCount=1
    )
    instance_id = response['Instances'][0]['InstanceId']
    print(f"Instance {instance_id} launched successfully.")
except ClientError as e:
    print(f"Error launching instance: {e}")

# Wait for the instance to be running
time.sleep(30)  # Wait for 30 seconds to allow the instance to start

# Step 2: Describe the instance
try:
    print("Describing the instance...")
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    instance_info = response['Reservations'][0]['Instances'][0]
    print(f"Instance ID: {instance_info['InstanceId']}")
    print(f"Instance State: {instance_info['State']['Name']}")
    print(f"Public IP Address: {instance_info.get('PublicIpAddress', 'N/A')}")
except ClientError as e:
    print(f"Error describing instance: {e}")

# Step 3: Stop the instance
try:
    print(f"Stopping instance {instance_id}...")
    ec2_client.stop_instances(InstanceIds=[instance_id])
    print(f"Instance {instance_id} is stopping...")
except ClientError as e:
    print(f"Error stopping instance: {e}")

# Wait for the instance to stop
time.sleep(30)

# Step 4: Start the instance
try:
    print(f"Starting instance {instance_id}...")
    ec2_client.start_instances(InstanceIds=[instance_id])
    print(f"Instance {instance_id} is starting...")
except ClientError as e:
    print(f"Error starting instance: {e}")

# Wait for the instance to start
time.sleep(30)

# Step 5: Terminate the instance
try:
    print(f"Terminating instance {instance_id}...")
    ec2_client.terminate_instances(InstanceIds=[instance_id])
    print(f"Instance {instance_id} is terminating...")
except ClientError as e:
    print(f"Error terminating instance: {e}")

# Wait for the instance to terminate
time.sleep(30)

print("Demo completed.")
