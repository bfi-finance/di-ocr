import ast
import os
from dotenv import load_dotenv

load_dotenv()
SERVER_HOST = os.environ.get("SERVER_HOST")
SERVER_PORT = int(os.environ.get("SERVER_PORT"))
LOG_LEVEL = f"{os.environ.get('LOG_LEVEL')}"
RELOAD = os.environ.get("RELOAD")
SERVICE_ACCOUNT_FILE_NAME = os.environ.get("SERVICE_ACCOUNT_FILE_NAME")
SERVICE_ACCOUNT_INFO = ast.literal_eval(os.environ.get("SERVICE_ACCOUNT_INFO"))


# print(type(SERVICE_ACCOUNT_FILE_NAME))
# print(type(SERVICE_ACCOUNT_INFO))
# print(SERVICE_ACCOUNT_INFO)