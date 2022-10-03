from unicodedata import name
from flask_wtf import FlaskForm
from wtforms import FileField, SelectField

from src.models.classesModel import ClassesModel

class TimetableForm(FlaskForm):
    form =SelectField(label='class', name ='form', id ='form')
    purpose =SelectField(label='type', name ='purpose', id ='purpose', choices=[('Teaching', 'Teaching'), ('Exam', 'Exam')])
    content =FileField(label='file', name ='content', id ='content')

    def __init__(self, **kwargs):
        super(TimetableForm, self).__init__(**kwargs)
        class_choices =[(cls.id, cls) for cls in ClassesModel.objects.all()]
        self.form.choices =[('', 'select timetable class'), *class_choices]