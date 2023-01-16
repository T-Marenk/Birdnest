import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, '..', '.env'))
except FileNotFoundError:
    pass

DRONE_URL = os.getenv('DRONE_URL')
PILOTS_URL = os.getenv('PILOTS_URL')
