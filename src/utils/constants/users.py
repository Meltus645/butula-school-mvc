from flask_mongoengine.wtf import model_form
from src.models import StaffModel, StudentsModel

USER_TYPES =['students', 'staff']

USER_FIELDS ={
    'subjects': ['code', 'name'],
    'e-notes': [],
    'exams': [],
    'time-table': [],
    'school-calendar': []
}

USER_PLACEHOLDERS ={
    'subjects': {
        'code': 'Enter subject code e.g 101',
        'name': 'Enter subject name e.g english'
    }
}

USER_FORMS ={
    'students': model_form(StudentsModel),
    'staff': model_form(StaffModel)
}