from mongoengine import Document, StringField, ListField, ReferenceField
from .permissionsModel import PermissionsModel   

class GroupsModel(Document):
    name =StringField(required =True, max_length=64)
    permissions =ListField(ReferenceField(PermissionsModel), required =False)

    meta ={'collection': 'group', 'indexes': [{'fields': ['$name'], 'default_language': 'english'}]} 

    def __str__(self):
        return f'{self.name}'