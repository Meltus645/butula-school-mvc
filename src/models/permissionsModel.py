from mongoengine import Document, StringField 

class PermissionsModel(Document):
    name =StringField(required =True, max_length= 64)
    model =StringField(required =True)

    meta ={'collection': 'permission', 'indexes': [{'fields': ['$name'], 'default_language': 'english'}]} 

    def __str__(self): return f'{self.name}'