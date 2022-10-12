from mongoengine import Document, StringField, IntField

class SubjectsModel(Document):
    name =StringField(regex=r'^[a-zA-Z]+$', required =True, unique =True)
    code =IntField(required =True, unique =True)
    subject_type =StringField(required =True)  

    meta ={
        'collection': 'subject',
        'indexes': [{'fields': ['$name'], 'default_language': 'english'}]
    } 
    def __str__(self): return f'{self.name}'