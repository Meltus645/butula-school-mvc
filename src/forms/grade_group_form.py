from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, IntegerField, SelectField
from src.models import SubjectsModel, GradesModel

class GradeGroupForm(FlaskForm):
    label =StringField()
    subjects =SelectMultipleField()
    min_score = IntegerField()
    max_score =IntegerField()
    grade =SelectField()

    def __init__(self, data =None, **kwargs):
        super(GradeGroupForm, self).__init__(**kwargs)


