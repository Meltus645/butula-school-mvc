from flask_wtf import FlaskForm 
from wtforms import StringField, SelectField, FileField
from src.models import ClassesModel

class StudentForm(FlaskForm):
    name =StringField(label ="Student Name", name='name', id='name')
    phone =StringField(label ="Phone Number", name='phone', id='phone')
    admission_number =StringField(label ="Admission Number", name='admission_number', id='admission_number')
    birth_certificate_number =StringField(label ="Birth Certificate Number", name='birth_certificate_number', id='birth_certificate_number')
    form =SelectField(label ="Student Class", name='form', id='form')
    avatar =FileField(label ="Passport Photo", name='avatar', id='avatar')

    def __init__(self, **kwargs):
        super(StudentForm, self).__init__(**kwargs)
        class_choices =[(cls.id, cls) for cls in ClassesModel.objects.all()]  
        self.form.choices =[('', 'Select student class'), *class_choices]
  