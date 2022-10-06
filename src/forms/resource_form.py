from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, SelectField, TextAreaField, DateTimeField, FileField
from src.models import SubjectsModel, ClassesModel, StaffModel
 
 

class ResourceForm(FlaskForm):
    topic =StringField(label='Topic', name= 'topic', id= 'topic')
    subject =SelectField(label='Subject', name ='subject', id ='subject', choices=[('', 'select resource subject')])
    resource_type =SelectField(label= 'Type', name ='resource_type', id ='resource_type', choices=[('', 'select resource type'),('Summary Notes', 'Summary Notes'),('RAT', 'RAT'),('Assignment', 'Assignment'),('Past Paper', 'Past Paper')])
    # submit_by =DateTimeField(label= 'Submit By', name ='submit_by', id ='submit_by')
    audience =SelectMultipleField(label='Audience', name ='audience', id ='audience')
    description =TextAreaField(label='Description or Instructions',id='description', name= 'description')
    author =SelectField(label='Author', name ='author', id ='author', choices=[('', 'select resource author')]) 
    file =FileField(label= 'Resource File', name ='file', id='file')

    def __init__(self, data =None, **kwargs):
        super(ResourceForm, self).__init__(**kwargs)
        subjects = [(subject.id, subject) for subject in SubjectsModel.objects.all()] 
        self.subject.choices =[*self.subject.choices, *subjects]  
        self.audience.choices =[(audience.id, audience) for audience in ClassesModel.objects.all()]
        self.author.choices =[*self.author.choices, *[(author.id, author) for author in StaffModel.objects.all()]]
        if data: 
            self.topic.default =data.topic
            self.subject.default =data.subject.id
            self.resource_type.default =data.resource_type
            self.audience.default =[audience.id for audience in data.audience]
            self.description.default =data.description
            self.author.default =data.author.id
            # self.submit_by.default =data.submit_by 

            self.process()



  