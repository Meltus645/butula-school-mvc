from mongoengine import Document, StringField, EmailField, ListField, ReferenceField, IntField
from .classesModel import ClassesModel
from .subjectsModel import SubjectsModel

class StudentsModel(Document):
    name =StringField(regex=r'^[a-zA-Z]+$', required =True, max_length=128) 
    birth_certificate_number =StringField(required =True, max_length=16)
    gender =StringField(required =False, max_length=6, regex=r'^[a-zA-Z]+$', default ='Male') 
    phone =StringField(regex=r'^[a-zA-Z]+$', required =True, unique =True, max_length=13)
    email =EmailField(required =False, unique =True)
    admission_number =IntField(required =True)
    form =ReferenceField(ClassesModel,required =True)
    subjects =ListField(ReferenceField(SubjectsModel)) 
    status =StringField(max_length="8", default ="Inactive", required =False, regex=r'^[a-zA-Z]+$')
    password =StringField(max_length=255, required =True)
    avatar =StringField(required =False) # http://127.0.0.1:8080/media/imgs/7043_date_uploaded.jpg
    
    meta ={
        'collection': 'staff',
        'indexes': [{'fields': ['$name', '$email', '$group'], 'default_language': 'english'}]
    }

    def save(self, force_insert=False, validate=True, clean=True, write_concern=None, cascade=None, cascade_kwargs=None, _refs=None, save_condition=None, signal_kwargs=None, **kwargs):
        return super().save(force_insert, validate, clean, write_concern, cascade, cascade_kwargs, _refs, save_condition, signal_kwargs, **kwargs)