from mongoengine import Document, StringField, IntField

class ClassesModel(Document):
    form =IntField(required =True)
    stream =StringField(required =True) 
    max_number_of_students =IntField(required =False)

    meta ={'collection': 'class'}