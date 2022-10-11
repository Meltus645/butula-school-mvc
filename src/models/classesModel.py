from mongoengine import Document, StringField, IntField

class ClassesModel(Document):
    form =IntField(required =True, min_value=1, max_value=6)
    stream =StringField(required =True, regex=r'^[A-Za-z]+$')  

    meta ={'collection': 'class', 'indexes': [{'fields': ['$form', '$stream'], 'default_language': 'english'}]}

    def __str__(self): return f'{self.form} {self.stream}'