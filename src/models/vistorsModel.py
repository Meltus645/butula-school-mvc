from mongoengine import Document, StringField, DateTimeField
from datetime import datetime

class VistorsModel(Document):
    signature =StringField() 
    client_name =StringField()
    client_version =StringField()
    device =StringField()
    model =StringField()
    os_name =StringField()
    os_version =StringField()
    first_visit =DateTimeField(required =False, default=datetime.now())

    meta ={'collection': 'visitor'} 

    def __str__(self):
        return f'{self.client_name}'