from src.forms.studentsForm import StudentForm
from src.forms.staffForm import StaffForm
from .app import ACTIONS

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
    'students': StudentForm,
    'staff': StaffForm
}