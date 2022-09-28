from flask_wtf import FlaskForm 
from wtforms import StringField, FileField, SelectField, EmailField 

class StaffForm(FlaskForm):
    name =StringField(label='Name',name= 'name', id= 'name')
    staffid =StringField(label = 'Staff ID', name= 'staffid', id= 'staffid')
    gender =SelectField(label = 'Gender', name= 'gender', id= 'gender', choices=(('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')))
    phone =StringField(label ="Phone Number", name= 'phone', id= 'phone')
    email =EmailField(label ="Email Address", name= 'email', id= 'email')
    avatar =FileField(label='Profile Picture', name= 'avatar', id='avatar')