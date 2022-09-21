from mongoengine import Document, ListField, ReferenceField, DictField, DateTimeField, BooleanField
from .studentsModel import StudentsModel
from .examsModel import ExamsModel
from .schoolCalendarModel import SchoolCalendarModel
from datetime import datetime

class ResultsModel(Document):
    calendar =ReferenceField(SchoolCalendarModel, required =True)
    exam =ReferenceField(ExamsModel, required =True)
    student =ReferenceField(StudentsModel, required =True)
    report =ListField(DictField(), required =True) #[{'subject': 'english', 'score': '72', 'grade': 'A}, ...]
    published =BooleanField(default=False, required =False)
    time_uploaded =DateTimeField(required=False, default=datetime.now())   

    meta ={'collection': 'results'}
     