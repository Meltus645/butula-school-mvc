from flask_wtf import FlaskForm 
from wtforms import StringField, SelectField, FloatField  
from src.models import ExamsModel, SchoolCalendarModel

# class SubjectFields(FlaskForm):
#     def __init__(self):
#         super(SubjectFields, self)

class ResultsForm(FlaskForm):
    calendar =SelectField(label ="Year and Term", name ='calendar', id ='calendar', choices=[('', 'Select year and term the exam was done')])
    exam =SelectField(label= "Exam", name ="exam", id ="exam", choices=[('', 'Select exam')]) 
    subjects =['english', 'kiswahili', 'mathematics']
    def __init__(self, student_id, data =None, **kwargs): 
        super(ResultsForm, self).__init__(**kwargs) 
        # for subject in self.subjects:  
        #     setattr(self, subject, FloatField(label=subject, name =subject, id =subject))  
        self.calendar.choices =[*self.calendar.choices, *[(calendar.id, calendar) for calendar in SchoolCalendarModel.objects.all()]] 
        self.exam.choices =[*self.exam.choices, *[(exam.id, exam) for exam in ExamsModel.objects.all()]]  
         
        if data: pass 
 