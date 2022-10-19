from mongoengine import EmbeddedDocument, ReferenceField, StringField, FloatField 
from .gradesModel import GradesModel
from .subjectsModel import SubjectsModel

class SubjectScoreModel(EmbeddedDocument): 
    subject =ReferenceField(SubjectsModel, required =True)
    score =FloatField(required =True) 
    grade =ReferenceField(GradesModel, required =True) 

    def __str__(self)->str:  return f'{self.score}'

