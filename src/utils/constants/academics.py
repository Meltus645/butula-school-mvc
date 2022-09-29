from src.forms.subjectForm import SubjectForm  

ACADEMIC_SECTIONS =['e-notes', 'subjects', 'exams', 'time-table', 'school-calendar'] 

ACADEMIC_FIELDS ={
    'subjects': ['code', 'name'],
    'e-notes': [],
    'exams': [],
    'time-table': [],
    'school-calendar': []
}

ACADEMIC_PLACEHOLDERS ={
    'subjects': {
        'code': 'Enter subject code e.g 101',
        'name': 'Enter subject name e.g english'
    },
    'e-notes': {},
    'exams': {},
    'time-table': {},
    'school-calendar': {}

}

ACADEMIC_FORMS ={
    'subjects': SubjectForm,
    'e-notes': None,
    'exams': None,
    'time-table': None,
    'school-calendar': None
}