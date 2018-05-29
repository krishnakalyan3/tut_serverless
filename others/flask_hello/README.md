# The Serveless Framework Tutorial

Installation pre-requisites

```
sudo apt-get update
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install -y nodejs python3.6 npm awscli python3-pip python3-venv
```

Node dependencies for deploying flask applications

```
# Installs the serverless framework
sudo npm i npm
sudo npm install -g serverless

# Init the project
npm init -f

# Install deps for flask
npm install --save-dev serverless-wsgi serverless-python-requirements
```

AWS credentials setup

```
Note:
IAM create a user `serverless-admin` with `AdministratorAccess`.

# Configure the keys for aws
aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-east-1
Default output format [None]:

```

Create a Virtual Env in project folder

```
# Virtual Environment stuff
python3.6 -m venv env
source env/bin/activate
```

Finally
```
pip freeze > requirements.txt

# Create app.py
# sls deploy
```