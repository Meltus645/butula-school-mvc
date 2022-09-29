from pathlib import Path
from os import getenv
from webbrowser import get
from dotenv import load_dotenv

load_dotenv()

BASEDIR =Path(__file__).resolve().parent.parent.parent.parent
EMAIL =getenv('EMAIL_ADDRESS')
PASSWORD =getenv('EMAIL_PASSWORD') 
ACTIONS =['list', 'new', 'edit', 'view', 'delete']