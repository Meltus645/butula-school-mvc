from mongoengine import Document, StringField, DateTimeField, ReferenceField, DictField, ListField  
from datetime import datetime
from .vistorsModel import VistorsModel

class VistorsSessionModel(Document):
    session_id =StringField(unique =True)
    visitor =ReferenceField(VistorsModel, required =True)
    time_started =DateTimeField(required=True, default=datetime.now())
    time_ended =DateTimeField(required=True)
    ip_address =StringField(required =True, regex =r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$") # ipv4
    pages =ListField(DictField(required =True)) #[{'name': 'page name', 'hits': 0, 'ref': 'referrer'}]
  
    meta ={'collection': 'visitor_session'} 
    def __str__(self): return f'{self.ip_address}'