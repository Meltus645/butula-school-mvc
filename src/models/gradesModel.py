from mongoengine import Document, StringField, IntField


class GradesModel(Document): 
    grade =StringField(regex=r'^[A-E][\-\+]?$', required =True, unique =True)
    points =IntField(required =True, min_value=1, max_value=12, unique =True)

    meta ={
        'collection': 'grades',
        'indexes': [{
            'fields': ['$grade', '$points'],
        }],
    }
    def __str__(self): return self.grade