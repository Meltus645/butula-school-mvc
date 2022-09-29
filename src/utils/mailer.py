import smtplib, ssl
from src.utils.constants.global import EMAIL, PASSWORD

class Mailer(smtplib):
    REPORT ={
        'sent': False, 'status_code': '400', 'message': 'Email not Sent'
    }
    def __init__(self, debug =True): 
        PORT =465
        context =ssl.create_default_context()
        if debug:
            pass
        else:
            with smtplib.SMTP_SSL("smtp.gmail.com", PORT, context=context) as server: 
                server.login(EMAIL, PASSWORD)
    def connect(self): pass
    def send(self): pass

def mailer(debug =True):
    pass