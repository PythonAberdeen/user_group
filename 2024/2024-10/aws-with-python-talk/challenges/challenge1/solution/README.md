# Walk Through

First we need an S3 bucket, this assumes you create one either via boto3 or the console.

The challenge asks for:
> Write a Python script that uploads files from your local system to an S3 bucket daily.

The solution script is in `challenge1.py`.

Since it asks for the script to be run daily, you'd need to run this on a scheduler.

For Mac/ Linux:

```
crontab -e
0 2 * * * path/to/your/venv/bin/python3 /path/to/your/script.py
``` 

For Windows:
- Open Task Scheduler.
- Create a new task and set the trigger to daily at a specific time.
- Set the action to start a program and point to your Python executable and the path to your script.

> Use versioning in S3 to manage changes to the files.

We need to enable versioning on our S3 bucket. 

We can do this via the console or the CLI, like:

```bash
aws s3api put-bucket-versioning --bucket your-bucket-name --versioning-configuration Status=Enabled
```

> Advanced: Implement a mechanism to automatically delete files that are older than 30 days.

The script does this with the following snippets.

List the object versions:

```
response = s3_client.list_object_versions(Bucket=BUCKET_NAME)
```

Based on the RETENTION_DAYS (30), find expired objects and delete them:

```
if (current_time - last_modified).days > RETENTION_DAYS:
    s3_client.delete_object(Bucket=BUCKET_NAME, Key=version['Key'], VersionId=version['VersionId'])

```