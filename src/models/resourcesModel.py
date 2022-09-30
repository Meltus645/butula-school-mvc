from mongoengine import Document, StringField, ReferenceField, ListField, DateTimeField, IntField
from .staffModel import StaffModel
from .subjectsModel import SubjectsModel
from .classesModel import ClassesModel

class ResourcesModel(Document):
    topic =StringField(required =True)  
    subject =ReferenceField(SubjectsModel, required =True)
    audience =ListField(ReferenceField(ClassesModel), required =True)
    description =StringField(required =True, max_length=256)
    resource_type =StringField(required =True, choices =(('Summary Notes', 'Summary Notes'),('RAT', 'RAT'),('Assignment', 'Assignment'),('Past Paper', 'Past Paper'),)) #[Assignment/RAT/CAT/Revision/Notes/Past Paper]
    content =StringField(required =False)
    submit_by =DateTimeField(required=False) 
    file =StringField(max_length =255, required =False)
    author =ReferenceField(StaffModel, required =True)
    views =IntField(required =False, default =0)
    downloads =IntField(required =False, default =0)
    time_uploaded =DateTimeField(required =False)

    meta ={'collection': 'resources', 'indexes': [{'fields': ['$topic']}]}

    def save(self, force_insert=False, validate=True, clean=True, write_concern=None, cascade=None, cascade_kwargs=None, _refs=None, save_condition=None, signal_kwargs=None, **kwargs):
        return super().save(force_insert, validate, clean, write_concern, cascade, cascade_kwargs, _refs, save_condition, signal_kwargs, **kwargs)

    
    def __str__(self):
        return f'{self.topic}'