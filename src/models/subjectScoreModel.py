from mongoengine import EmbeddedDocument, ReferenceField, StringField, FloatField, IntField

class SubjectScoreModel(EmbeddedDocument): 
    subject =ReferenceField('SubjectsModel', required =True)
    score =FloatField(required =True, default =0.0) 
    grade =StringField(required =False, default ='E')
    points =IntField(required =False, default =0)

    def __str__(self)->str:  return f'{self.score}'

