from mongoengine import Document, StringField, EmailField, ListField, ReferenceField, DictField
from .groupsModel import GroupsModel, PermissionsModel
from .rolesModel import RolesModel

class StaffModel(Document):
    name =StringField(regex=r'^[a-zA-Z]+$', required =True, max_length=128) 
    staffid =StringField(regex=r'^[a-zA-Z]+$', required =True, max_length=128) 
    phone =StringField(regex=r'^[a-zA-Z]+$', required =True, unique =True, max_length=13)
    email =DictField(required =True) #{'address': '', 'verified': False} 
    gender =StringField(required =True, max_length=6, regex=r'^[a-zA-Z]+$')
    role =ListField(ReferenceField(RolesModel), required =False) 
    group =ListField(ReferenceField(GroupsModel), required =False)
    permissions =ListField(ReferenceField(PermissionsModel), required =False)
    status =StringField(max_length="8", default ="Inactive", required =False, regex=r'^[a-zA-Z]+$')
    Otp =DictField(required =False) #{'code': 1234, 'expires': ''}  
    password =StringField(max_length=255)
    avatar =StringField(required =False) # http://127.0.0.1:8080/media/imgs/7043_date_uploaded.jpg
 
    meta ={
        'collection': 'staff',
        'indexes': [{'fields': ['$name', '$email', '$group'], 'default_language': 'english'}]
    }

    def save(self, force_insert=False, validate=True, clean=True, write_concern=None, cascade=None, cascade_kwargs=None, _refs=None, save_condition=None, signal_kwargs=None, **kwargs):
        return super().save(force_insert, validate, clean, write_concern, cascade, cascade_kwargs, _refs, save_condition, signal_kwargs, **kwargs)