from flask_wtf import FlaskForm
from wtforms import StringField, SelectField  

class ExamForm(FlaskForm):
    exam_name =StringField(label='Name', name ='exam_name', id ='exam_name')
    exam_type =SelectField(label='Type', name ='exam_type', id ='exam_type', choices=[('Internal', 'Internal'), ('External', 'External')])
      
    def __init__(self, data =None, **kwargs):
        super(ExamForm, self).__init__(**kwargs) 
         
        if data: 
            self.exam_name.default =data.exam_name  
            self.exam_type.default =data.exam_type  
            self.process()
