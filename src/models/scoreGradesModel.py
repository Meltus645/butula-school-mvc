from mongoengine import EmbeddedDocument, StringField, ReferenceField
from .gradesModel import GradesModel 

class ScoreGradesModel(EmbeddedDocument): 
    score_range =StringField(regex=r'^[0-9]{2,3}-[0-9]{2,3}$', required =True)
    grade =ReferenceField(GradesModel, required =True)

    def __str__(self): return self.grade.grade