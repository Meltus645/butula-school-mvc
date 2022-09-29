from unicodedata import name
from flask_wtf import FlaskForm 
from wtforms import StringField, IntegerField 

class SubjectForm(FlaskForm):
    name =StringField(label= 'Subject Name', id ='name', name ='name')
    code =IntegerField(label= 'Subject Code', id ='code', name ='code')
