from email.policy import default
from mongoengine import EmbeddedDocument,ReferenceField, DateTimeField, BooleanField, StringField, EmbeddedDocumentListField 

from .subjectScoreModel import SubjectScoreModel
from .examsModel import ExamsModel
from .schoolCalendarModel import SchoolCalendarModel 
from datetime import datetime

class ResultsModel(EmbeddedDocument):
    calendar =ReferenceField(SchoolCalendarModel, required =True)
    exam =ReferenceField(ExamsModel, required =True) 
    scores =EmbeddedDocumentListField(SubjectScoreModel, required =True)  
    meangrade =StringField(required =False, default ='E')
    published =BooleanField(default=False, required =False)
    time_uploaded =DateTimeField(required=False, default=datetime.now())   

    def __str__(self): return f'{self.meangrade}'
