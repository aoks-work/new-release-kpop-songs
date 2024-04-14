from dotenv import load_dotenv
load_dotenv()

import os

CLIENT_ID = os.getenv('CLIENT_ID') 
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USER_NAME = os.getenv('USER_NAME')
SHEET_ID = os.getenv('SHEET_ID')