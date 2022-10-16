from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from src.models import StaffModel  

class DepartmentForm(FlaskForm):
    name =StringField(label='Department name', name ='name', id ='name')
    head =SelectField(label='Department head', name ='head', id ='head', choices=[('', 'Select the head of this department')])
      
    def __init__(self, data =None, **kwargs):
        super(DepartmentForm, self).__init__(**kwargs) 
        head_choices =[(head.id, head.name) for head in StaffModel.objects.all()] 
        self.head.choices =[*self.head.choices, *head_choices]
        if data: 
            self.name.default =data.name  
            self.head.default =data.head.id  
            self.process()
