import os
from dotenv import load_dotenv

dotenv_path = os.path.join('', '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

API_KEY = os.environ.get('API_KEY')
