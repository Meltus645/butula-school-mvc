from mongoengine import Document, StringField, ListField, ReferenceField, DictField, EmailField, BooleanField, DateTimeField
from datetime import datetime
from .groupsModel import GroupsModel, PermissionsModel
from .rolesModel import RolesModel

class StaffModel(Document):
    name =StringField(regex=r'^[a-zA-Z ]+$', required =True, max_length=128) 
    staff_id =StringField(regex=r'^[0-9]+$', required =True, max_length=128) 
    phone =StringField(regex=r'^[0-9]+$', required =True, unique =True, max_length=13)
    email =EmailField(required =True, max_length =64)
    gender =StringField(required =True, max_length=6, regex=r'^[a-zA-Z]+$', choices =(('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')))
    role =ListField(ReferenceField(RolesModel), required =False) 
    group =ListField(ReferenceField(GroupsModel), required =False)
    permissions =ListField(ReferenceField(PermissionsModel), required =False)
    status =StringField(max_length=8, default ="Inactive", required =False, regex=r'^[a-zA-Z]+$')
    otp =DictField(required =False) #{'code': 1234, 'expires': ''} 
    email_verified =BooleanField(required=True, default=False) 
    password =StringField(max_length=255)
    created =DateTimeField(required=True, default=datetime.now)
    avatar =StringField(required =False) 
    filename =StringField(max_length =64, required =False)
 
    meta ={
        'collection': 'staff',
        'indexes': [{'fields': ['$name', '$email', '$group'], 'default_language': 'english'}]
    } 
    
    def __str__(self):
        return f'{self.name}'