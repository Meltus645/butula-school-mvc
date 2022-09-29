from src.forms.subjectForm import SubjectForm  
from src.forms.examForm import ExamForm

ACADEMIC_SECTIONS =['e-notes', 'subjects', 'exams', 'time-table', 'school-calendar'] 

ACADEMIC_FIELDS ={
    'subjects': ['code', 'name'],
    'e-notes': [],
    'exams': ['exam_name', 'exam_type'],
    'time-table': [],
    'school-calendar': []
}

ACADEMIC_PLACEHOLDERS ={
    'subjects': {
        'code': 'Enter subject code e.g 101',
        'name': 'Enter subject name e.g english'
    },
    'e-notes': {},
    'exams': {
        'exam_name': 'Enter Exam Name e.g C.A.T 1', 
    },
    'time-table': {},
    'school-calendar': {}

}

ACADEMIC_FORMS ={
    'subjects': SubjectForm,
    'e-notes': None,
    'exams': ExamForm,
    'time-table': None,
    'school-calendar': None
}