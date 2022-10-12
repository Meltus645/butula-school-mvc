from unicodedata import name
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FloatField  
from src.models import ExamsModel, SchoolCalendarModel

class ResultsForm(FlaskForm):
    calendar =SelectField(label ="Year and Term", name ='calendar', id ='calendar', choices=[('', 'Select year and term the exam was done')])
    exam =SelectField(label= "Exam", name ="exam", id ="exam", choices=[('', 'Select exam')]) 
    subjects =['english', 'kiswahili', 'mathematics']
    # for subject in subjects:  setattr(FlaskForm, subject, FloatField(label=subject, name =subject, id =subject))  
    def __init__(self, data =None, **kwargs):
        super(ResultsForm, self).__init__(**kwargs)
        self.calendar.choices =[*self.calendar.choices, *[(calendar.id, calendar) for calendar in SchoolCalendarModel.objects.all()]] 
        self.exam.choices =[*self.exam.choices, *[(exam.id, exam) for exam in ExamsModel.objects.all()]]  
        
        if data: pass