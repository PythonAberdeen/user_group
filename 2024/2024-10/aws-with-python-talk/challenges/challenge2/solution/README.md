# Walk Through

> Create a basic Flask or Django web app.

A simple Flask app is in the variable `USER_DATA_SCRIPT`.

> Use boto3 to automate launching an EC2 instance and deploy the web app on it.

The solution code is in the file `launch_ec2.py`.

You will have to replace `my-key-pair` with the name of your EC2 key pair.

> Ensure the app is accessible via a public IP.

`ec2.create_instances` launches the EC2 instance and our app is run on port 80.

Going to http://<The EC2's public IP address> should display:

![alt text](image.png)