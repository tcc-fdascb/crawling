# settings.py
from dotenv import load_dotenv
load_dotenv()

import os

username = os.getenv('MONGODB_USER')
password = os.getenv('MONGODB_PASS')

print(username)
print(password)
