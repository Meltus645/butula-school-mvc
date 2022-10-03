from dotenv import load_dotenv
from os import getenv 

load_dotenv()
SECRET_KEY =getenv('SECRET_KEY')
MONGODB_SETTINGS =[{'db': getenv('DBS'), 'host': getenv('DBS_HOST'), 'port': int(getenv('DBS_PORT')),  'connect': False}] 