from unicodedata import name
from flask_wtf import FlaskForm
from wtforms import FileField, SelectField, HiddenField

from src.models.classesModel import ClassesModel

class TimetableForm(FlaskForm):
    form =SelectField(label='class', name ='form', id ='form')
    purpose =SelectField(label='type', name ='purpose', id ='purpose', choices=[('Teaching', 'Teaching'), ('Exam', 'Exam')])
    file =FileField(label='file', name ='file', id ='file') 

    def __init__(self, data =None, **kwargs):
        super(TimetableForm, self).__init__(**kwargs)
        class_choices =[(cls.id, cls) for cls in ClassesModel.objects.all()] 
        self.form.choices =[('', 'select timetable class'), *class_choices] 
         
        if data: 
            self.form.default =data.form.id   
            self.purpose.default =data.purpose 
            self.hidden_field =HiddenField(label='', name='hidden_field', id='hidden_field', default=data.file)
            data.filename ='_'.join(data.file.split('/')[-1].split('_')[1:])  
            self.process()