from mongoengine import Document, ReferenceField, StringField
from .classesModel import ClassesModel


class TimetableModel(Document):
    form =ReferenceField(ClassesModel, required =True)
    purpose =StringField(required =True, max_length=32) 
    file =StringField(required =True) 
    filename =StringField(required =True, max_length=64) 

    meta ={'collection': 'timetable', 'indexes': [{'fields': ['$form', '$purpose'], 'default_language': 'english'}]}

    def __str__(self):
        return f'{self.form} {self.purpose} timetable'