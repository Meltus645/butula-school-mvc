from flask_wtf import FlaskForm 
from wtforms import StringField, SelectField 

class ClassForm(FlaskForm):
    form =StringField(label='Form', name ='form', id ='form')
    stream =SelectField(label='Stream', name ='stream', id ='stream', choices=(('North', 'North'), ('East', 'East'), ('South', 'South'), ('West', 'West'),('Central', 'Central')))