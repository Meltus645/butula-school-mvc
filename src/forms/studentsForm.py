from flask_wtf import FlaskForm 
from wtforms import StringField, FileField, SelectField 

class StudentForm(FlaskForm):
    name =StringField(label='Student Name',name= 'name', id= 'name')
    admission_number =StringField(label = 'Admission Number', name= 'admission_number', id= 'admission_number')
    phone =StringField(label ="Parent/Guadian Phone Number", name= 'phone', id= 'phone')
    birth_certificate_number =StringField(label='Birth Certificate Number', name='birth_certificate_number', id='birth_certificate_number')
    form =SelectField(label= 'Student class', name ='form', id ='form', choices=(('Form 1 West', '1w',)))
    avatar =FileField(label='Student Passport Photo', name= 'avatar', id='avatar')