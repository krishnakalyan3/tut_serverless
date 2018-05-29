# AWS Serverless deployement

Download AWS CLI
```
apt-get update && apt-get install awscli

# Create a user with adminstrator access
aws configure

# Check 
cat .aws/credentials
```


Node Modules
```
npm install serverless-python-requirements
npm install serverless-wsgi
```

Running the App Locally
```
sudo pip3 install -r requirements.txt
python3 app.py
```

App with serveless module
```
sls wsgi serve
```
