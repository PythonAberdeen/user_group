# aws-with-python-talk

## Demos

Demos are:
- hello_world.py
    - this expects you have ran aws configure
- s3.py
    - a file name `sample.txt`
- ec2.py
    - this needs an EC2 key pair
- lambda.py
    - this needs an IAM role

# Challenges

The challenges are under `challenges/`.

e.g. 

```
- challenge1/
 |- README.md - description of what to do
 |- solution/
  -|
   |- README.md - walk through of challenge
   |- *Solution
```

## Set up your virutal environment

```python

# 1. Ensure you have Python installed
python --version
# If you don't, install from https://www.python.org/downloads/

# 2. Create a virtual environment
python -m venv venv

# 3. Active the virutal environment

# On Windows
venv\Scripts\activate

# On macos / Linux
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Once finished, deactivate the virutal enviroxnment
deactivate

```