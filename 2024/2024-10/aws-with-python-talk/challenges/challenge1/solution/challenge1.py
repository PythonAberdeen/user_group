import boto3
import os
import datetime
from botocore.exceptions import NoCredentialsError

# Constants
BUCKET_NAME = 'my-aws-bucket-031024'
LOCAL_DIRECTORY = './local_dir'  # Change this to your local directory path
RETENTION_DAYS = 30

# Initialize the S3 client
s3_client = boto3.client('s3')

def upload_files_to_s3():
    """Uploads files from the local directory to S3."""
    try:
        for filename in os.listdir(LOCAL_DIRECTORY):
            file_path = os.path.join(LOCAL_DIRECTORY, filename)
            if os.path.isfile(file_path):
                s3_client.upload_file(file_path, BUCKET_NAME, filename)
                print(f"Uploaded {filename} to S3 bucket {BUCKET_NAME}.")
    except FileNotFoundError:
        print("The local directory does not exist.")
    except NoCredentialsError:
        print("Credentials not available.")

def delete_old_versions():
    """Deletes files from S3 that are older than RETENTION_DAYS."""
    try:
        response = s3_client.list_object_versions(Bucket=BUCKET_NAME)
        
        if 'Versions' in response:
            current_time = datetime.datetime.now(datetime.timezone.utc)
            for version in response['Versions']:
                last_modified = version['LastModified']
                if (current_time - last_modified).days > RETENTION_DAYS:
                    s3_client.delete_object(Bucket=BUCKET_NAME, Key=version['Key'], VersionId=version['VersionId'])
                    print(f"Deleted old version of {version['Key']} with VersionId {version['VersionId']}.")
    except NoCredentialsError:
        print("Credentials not available.")

if __name__ == "__main__":
    upload_files_to_s3()
    delete_old_versions()
