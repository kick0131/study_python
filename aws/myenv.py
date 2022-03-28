import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

AWS_PROFILE = os.environ.get("AWS_PROFILE")
DYNAMODB_TABLE = os.environ.get("DYNAMODB_TABLE")

COGNITO_USER_POOL_ID = os.environ.get("COGNITO_USER_POOL_ID")
COGNITO_CLIENT_ID = os.environ.get("COGNITO_CLIENT_ID")
COGNITO_USER_ID = os.environ.get("COGNITO_USER_ID")
COGNITO_EMAIL = os.environ.get("COGNITO_EMAIL")
COGNITO_PASSWORD = os.environ.get("COGNITO_PASSWORD")
COGNITO_CONFIRM_CODE = os.environ.get("COGNITO_CONFIRM_CODE")
COGNITO_ATTRIBUTES = os.environ.get("COGNITO_ATTRIBUTES")
