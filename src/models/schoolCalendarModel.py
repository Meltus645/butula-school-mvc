from mongoengine import Document, StringField, DateField, IntField

class SchoolCalendarModel(Document):
    year =StringField(required =True, regex=r"^20[0-9]{2}$")
    term =IntField(required =True, min_value=1, max_value=3)
    starts_from =DateField(required=True, unique=True)
    ends_on =DateField(required =True, unique=True)
    
    meta ={'collection': 'calendar'}
    def __str__(self): return f'{self.year} term {self.term}'