from flask_wtf import FlaskForm 
from wtforms import StringField, SelectField 

class ExamForm(FlaskForm):
    exam_name =StringField(label='Exam Name', name ='exam_name', id ='exam_name')
    exam_type =SelectField(label='Exam Type', name ='exam_type', id ='exam_type', choices=(('Internal', 'Internal'), ('External', 'External')))