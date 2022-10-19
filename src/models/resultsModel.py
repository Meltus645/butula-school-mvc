from email.policy import default
from mongoengine import EmbeddedDocument,ReferenceField, DateTimeField, BooleanField, StringField, EmbeddedDocumentListField 
from datetime import datetime

from .subjectScoreModel import SubjectScoreModel
from .examsModel import ExamsModel
from .schoolCalendarModel import SchoolCalendarModel 

class ResultsModel(EmbeddedDocument):
    calendar =ReferenceField(SchoolCalendarModel, required =True)
    exam =ReferenceField(ExamsModel, required =True) 
    scores =EmbeddedDocumentListField(SubjectScoreModel, required =True)  
    """ 
    Grading: [
        A: 12, A-:11,
        
    ]
    """ 
    meangrade =StringField(required =False, default ='E')
    published =BooleanField(default=False, required =False)
    time_uploaded =DateTimeField(required=False, default=datetime.now())   

    def __str__(self): return f'{self.meangrade}'
