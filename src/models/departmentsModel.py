from mongoengine import Document, StringField, ReferenceField 
from .staffModel import StaffModel

class DepartmentsModel(Document):
    name =StringField(max_length=24, required =True, regex=r'[a-zA-Z ]+', unique =True)  
    head =ReferenceField(StaffModel, required =True)
 
    meta ={'collection': 'departments', 'indexes': [{'fields': ['$name'], 'default_language': 'english'}]}

    def __str__(self): return f'{self.name}'