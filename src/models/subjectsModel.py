from mongoengine import Document, StringField, IntField

class SubjectsModel(Document):
    name =StringField(regex=r'^[a-zA-Z]+$', required =True, unique =True)
    code =IntField(required =True, unique =True)

    meta ={
        'collection': 'subject',
        'indexes': [{'fields': ['$name'], 'default_language': 'english'}]
    }