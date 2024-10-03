import boto3
import time

# AWS Configuration
REGION = 'eu-west-2'  # London
AMI_ID = 'ami-0b45ae66668865cd6'  # Amazon Linux
INSTANCE_TYPE = 't2.micro'
KEY_NAME = 'my-key-pair'  # Replace with your key pair name
SECURITY_GROUP_NAME = 'flask-app-sg'
USER_DATA_SCRIPT = '''#!/bin/bash
yum update -y
yum install -y python3 pip
pip3 install Flask
mkdir /home/ec2-user/my_flask_app
cd /home/ec2-user/my_flask_app
echo "from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'Hello, World! This is my Flask app running on EC2!'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)" > app.py
nohup python3 app.py &
'''

# Create a new EC2 instance
ec2 = boto3.resource('ec2', region_name=REGION)

# Create a security group
security_group = ec2.create_security_group(GroupName=SECURITY_GROUP_NAME, Description='Allow HTTP traffic')
security_group.authorize_ingress(IpProtocol='tcp', FromPort=80, ToPort=80, CidrIp='0.0.0.0/0')

# Launch the EC2 instance
instance = ec2.create_instances(
    ImageId=AMI_ID,
    InstanceType=INSTANCE_TYPE,
    KeyName=KEY_NAME,
    SecurityGroupIds=[security_group.id],
    MinCount=1,
    MaxCount=1,
    UserData=USER_DATA_SCRIPT
)

print(f'Launching EC2 instance with ID: {instance[0].id}')

# Wait for the instance to be running
instance[0].wait_until_running()
instance[0].reload()

print(f'EC2 instance is running at: {instance[0].public_ip_address}')
