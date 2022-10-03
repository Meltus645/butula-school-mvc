from mongoengine import Document, StringField, ListField, ReferenceField, DateTimeField
from datetime import datetime 
from .classesModel import ClassesModel
from .subjectsModel import SubjectsModel

class StudentsModel(Document):
    name =StringField(regex=r'^[a-zA-Z]+$', required =True, max_length=128) 
    birth_certificate_number =StringField(required =True, unique =True, regex=r'^[0-9]{13,}$', max_length=18)
    gender =StringField(required =False, max_length=6, regex=r'^[a-zA-Z]+$', default ='Male') 
    phone =StringField(regex=r'^[0-9]+$', required =True, unique =True, max_length=13) 
    admission_number =StringField(required =True, unique =True, regex=r'^[0-9]{4,6}$', max_length=6)
    form =ReferenceField(ClassesModel,required =True)
    subjects =ListField(ReferenceField(SubjectsModel), required =False) 
    status =StringField(max_length=8, default ="Inactive", required =False, regex=r'^[a-zA-Z]+$')
    password =StringField(max_length=255, required =True)
    enrolled =DateTimeField(required= False, default=datetime.now)
    avatar =StringField(required =False, max_length=64) # http://127.0.0.1:8080/media/imgs/7043_date_uploaded.jpg
    # 
    meta ={
        'collection': 'student',
        'indexes': [{'fields': ['$name', '$admission_number'], 'default_language': 'english'}]
    } 

    def save(self, force_insert=False, validate=True, clean=True, write_concern=None, cascade=None, cascade_kwargs=None, _refs=None, save_condition=None, signal_kwargs=None, **kwargs):
        return super().save(force_insert, validate, clean, write_concern, cascade, cascade_kwargs, _refs, save_condition, signal_kwargs, **kwargs)
    
    def __str__(self):
        return f'{self.name}'