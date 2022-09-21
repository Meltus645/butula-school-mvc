from mongoengine import Document, StringField, BooleanField, EmailField, DateTimeField, ListField, ReferenceField
from datetime import datetime
from .staffModel import StaffModel

class TicketsModel(Document):
    holder_name =StringField(required =True, max_length=64)
    holder_email =EmailField(required =True) 
    inquiry =StringField(required =True, max_length=360)
    read =BooleanField(required=False, default= False)
    viewed_by =ListField(ReferenceField(StaffModel))
    received =DateTimeField(required=False, default=datetime.now)

    meta ={'collection': 'ticket'}