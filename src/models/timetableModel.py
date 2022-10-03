from mongoengine import Document, ReferenceField, StringField
from .classesModel import ClassesModel


class TimetableModel(Document):
    form =ReferenceField(ClassesModel, required =True)
    purpose =StringField(required =True, choices =(('Teaching', 'Teaching'),('Exams', 'Exams')), default ='Teaching') 
    content =StringField(required =True, max_length=64) 

    meta ={'collection': 'timetable', 'indexes': [{'fields': ['$form', '$purpose'], 'default_language': 'english'}]}

    def __str__(self):
        return f'{self.form.name} {self.purpose} timetable'