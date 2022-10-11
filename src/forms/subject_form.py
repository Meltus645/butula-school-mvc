from email.policy import default
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField  

class SubjectForm(FlaskForm):
    name =StringField(label='Name', name ='name', id ='name')
    code =StringField(label='Code', name ='code', id ='code')
    subject_type =SelectField(label='Type', name ='subject_type', id ='subject_type', choices=[('', 'Specify if subject is compulsory or optional'),('Compulsory', 'Compulsory'), ('Optional', 'Optional')])

    def __init__(self, data =None, **kwargs):
        super(SubjectForm, self).__init__(**kwargs) 
        if data: 
            self.name.default =data.name  
            self.code.default =data.code  
            self.subject_type.default =data.subject_type  
            self.process()
