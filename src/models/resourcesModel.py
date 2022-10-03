from mongoengine import Document, StringField, ReferenceField, ListField, DateTimeField, IntField
from .staffModel import StaffModel
from .subjectsModel import SubjectsModel
from .classesModel import ClassesModel

class ResourcesModel(Document):
    topic =StringField(required =True, max_length=255)  
    subject =ReferenceField(SubjectsModel, required =True)
    audience =ListField(ReferenceField(ClassesModel), required =True)
    description =StringField(required =True, max_length=256)
    resource_type =StringField(required =True, choices =(('Summary Notes', 'Summary Notes'),('RAT', 'RAT'),('Assignment', 'Assignment'),('Past Paper', 'Past Paper'),)) #[Assignment/RAT/CAT/Revision/Notes/Past Paper]
    submit_by =DateTimeField(required=False) 
    file =StringField(max_length =255, required =False)
    author =ReferenceField(StaffModel, required =True)
    views =IntField(required =False, default =0)
    downloads =IntField(required =False, default =0)
    time_uploaded =DateTimeField(required =False)

    meta ={'collection': 'resources', 'indexes': [{'fields': ['$topic']}]}

     
    def __str__(self):
        return f'{self.topic}'