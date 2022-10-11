from mongoengine import Document, StringField, ListField, ReferenceField, DateTimeField
from datetime import datetime 
from .classesModel import ClassesModel
from .subjectsModel import SubjectsModel

class StudentsModel(Document):
    name =StringField(regex=r'^[a-zA-Z ]+$', required =True, max_length=128) 
    birth_certificate_number =StringField(required =True, unique =True, regex=r'^[0-9]{13,}$', max_length=18)
    gender =StringField(required =False, max_length=6, regex=r'^[a-zA-Z]+$', default ='Male') 
    phone =StringField(regex=r'^[0-9]+$', required =True, unique =True, max_length=13) 
    admission_number =StringField(required =True, unique =True, regex=r'^[0-9]{4,6}$', max_length=6)
    form =ReferenceField(ClassesModel,required =True)
    subjects =ListField(ReferenceField(SubjectsModel), required =False) 
    result =EmbeddedDocumentListField(ResultsModel, required =False, default =[])
    status =StringField(max_length=8, default ="Active", required =False, regex=r'^[a-zA-Z]+$')
    password =StringField(max_length=255, required =True)
    enrolled =DateTimeField(required= False, default=datetime.now)
    avatar =StringField(required =False) 
    filename =StringField(max_length =64, required =False)
    
    meta ={
        'collection': 'student',
        'indexes': [{'fields': ['$name', '$admission_number'], 'default_language': 'english'}]
    } 
    def __str__(self): return f"{self.admission_number} - {self.name.split(' ')[0]}" 