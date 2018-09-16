from dotenv import load_dotenv
import os

# Load our .env file to environment
load_dotenv()

# We got our access and secret key without hardcoding!
our_aws_access_key = os.getenv('AWS_ACCESS_KEY')
our_aws_secret_key = os.getenv('AWS_SECRET_KEY')
