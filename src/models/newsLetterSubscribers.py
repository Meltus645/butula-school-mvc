from mongoengine import Document, EmailField, DateTimeField 
from datetime import datetime 

class NewsLetterSubcribersModel(Document): 
    email =EmailField(required =True)  
    joined =DateTimeField(required=False, default=datetime.now)

    meta ={'collection': 'newsletter_subscriber'}


    def __str__(self): return f'{self.email}'