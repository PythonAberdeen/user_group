import boto3
import os
from botocore.exceptions import ClientError

# Initialize the S3 client
s3_client = boto3.client('s3')

# Define your bucket name and file paths
bucket_name = 'my-unique-bucket-name-123456'  # Must be globally unique
file_to_upload = 'sample.txt'  # The file you want to upload
downloaded_file = 'downloaded_sample.txt'  # The name for the downloaded file

# Step 1: Create a bucket
try:
    s3_client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': boto3.session.Session().region_name
        }
    )
    print(f"Bucket '{bucket_name}' created successfully.")
except ClientError as e:
    print(f"Error creating bucket: {e}")

# Step 2: Upload a file to the bucket
try:
    s3_client.upload_file(file_to_upload, bucket_name, os.path.basename(file_to_upload))
    print(f"File '{file_to_upload}' uploaded successfully to bucket '{bucket_name}'.")
except ClientError as e:
    print(f"Error uploading file: {e}")

# Step 3: List objects in the bucket
try:
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    print(f"Objects in bucket '{bucket_name}':")
    if 'Contents' in response:
        for obj in response['Contents']:
            print(f" - {obj['Key']}")
    else:
        print("No objects found.")
except ClientError as e:
    print(f"Error listing objects: {e}")

# Step 4: Download a file from the bucket
try:
    s3_client.download_file(bucket_name, os.path.basename(file_to_upload), downloaded_file)
    print(f"File '{os.path.basename(file_to_upload)}' downloaded successfully as '{downloaded_file}'.")
except ClientError as e:
    print(f"Error downloading file: {e}")

# Step 5: Delete the uploaded file from the bucket
try:
    s3_client.delete_object(Bucket=bucket_name, Key=os.path.basename(file_to_upload))
    print(f"File '{os.path.basename(file_to_upload)}' deleted successfully from bucket '{bucket_name}'.")
except ClientError as e:
    print(f"Error deleting file: {e}")

# Step 6: Delete the bucket
try:
    s3_client.delete_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' deleted successfully.")
except ClientError as e:
    print(f"Error deleting bucket: {e}")
