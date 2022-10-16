from email.policy import default
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField 
from src.models import DepartmentsModel 

class SubjectForm(FlaskForm):
    name =StringField(label='Name', name ='name', id ='name')
    code =StringField(label='Code', name ='code', id ='code')
    subject_type =SelectField(label='Type', name ='subject_type', id ='subject_type', choices=[('', 'Specify if subject is compulsory or optional'),('Compulsory', 'Compulsory'), ('Optional', 'Optional')])
    deparment =SelectField(label='Department', name ='department', id ='department', choices=[('', 'select department for the new subject')])

    def __init__(self, data =None, **kwargs):
        super(SubjectForm, self).__init__(**kwargs) 
        department_choices =[(department.id, department.name) for department in DepartmentsModel.objects.all().order_by('name')] 
        self.deparment.choices =[*self.deparment.choices, *department_choices]
        if data: 
            self.name.default =data.name  
            self.code.default =data.code  
            self.subject_type.default =data.subject_type  
            self.deparment.default =data.department.id  
            self.process()
