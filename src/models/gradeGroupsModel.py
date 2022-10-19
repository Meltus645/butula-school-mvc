from mongoengine import Document, ListField, ReferenceField, EmbeddedDocumentListField, StringField
from .subjectsModel import SubjectsModel 
from .scoreGradesModel import ScoreGradesModel


class GradeGroupModel(Document):
    label =StringField(regex =r'^[A-Za-z0-9\- ]+', required =True)
    subjects =ListField(ReferenceField(SubjectsModel), required =True) 
    grades =EmbeddedDocumentListField(ScoreGradesModel)

    

    def __str__(self): return self.label