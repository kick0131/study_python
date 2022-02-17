import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

AWS_PROFILE = os.environ.get("AWS_PROFILE")
DYNAMODB_TABLE = os.environ.get("DYNAMODB_TABLE")