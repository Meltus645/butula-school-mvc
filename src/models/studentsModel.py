from mongoengine import Document, StringField, EmailField, ListField, ReferenceField, IntField
from .classesModel import ClassesModel
from .subjectsModel import SubjectsModel

class StudentsModel(Document):
    name =StringField(regex=r'^[a-zA-Z]+$', required =True, max_length=128) 
    birth_certificate_number =StringField(required =True, max_length=16, unique =True)
    gender =StringField(required =False, max_length=6, regex=r'^[a-zA-Z]+$', default ='Male') 
    phone =StringField(regex=r'^[a-zA-Z]+$', required =True, unique =True, max_length=13) 
    admission_number =IntField(required =True, unique =True)
    form =ReferenceField(ClassesModel,required =True)
    subjects =ListField(ReferenceField(SubjectsModel), required =False) 
    status =StringField(max_length="8", default ="Inactive", required =False, regex=r'^[a-zA-Z]+$')
    password =StringField(max_length=255, required =True)
    avatar =StringField(required =False) # http://127.0.0.1:8080/media/imgs/7043_date_uploaded.jpg
    
    meta ={
        'collection': 'student',
        'indexes': [{'fields': ['$name', '$admission_number'], 'default_language': 'english'}]
    } 