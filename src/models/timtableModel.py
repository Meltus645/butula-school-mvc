from email.policy import default
from mongoengine import Document, ReferenceField, StringField, FileField
from .classesModel import ClassesModel


class TimetableModel(Document):
    form =ReferenceField(ClassesModel, required =True)
    purpose =StringField(required =True, choices =(('Teaching', 'Teaching'),('Exams', 'Exams')), default ='Teaching') 
    file =FileField(required =True)  

    meta ={'collection': 'timetable', 'indexes': [{'fields': ['$form', '$purpose'], 'default_language': 'english'}]}


    def save(self, force_insert=False, validate=True, clean=True, write_concern=None, cascade=None, cascade_kwargs=None, _refs=None, save_condition=None, signal_kwargs=None, **kwargs):
        return super().save(force_insert, validate, clean, write_concern, cascade, cascade_kwargs, _refs, save_condition, signal_kwargs, **kwargs)

    def __str__(self):
        return f'{self.form} {self.purpose} timetable'