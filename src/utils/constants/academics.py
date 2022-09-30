from src.forms.subjectForm import SubjectForm  
from src.forms.examForm import ExamForm
from src.forms.classForm import ClassForm

from src.models.classesModel import ClassesModel
from src.models.examsModel import ExamsModel
from src.models.resourcesModel import ResourcesModel
from src.models.schoolCalendarModel import SchoolCalendarModel
from src.models.subjectsModel import SubjectsModel 


ACADEMIC_SECTIONS =['e-notes', 'subjects', 'exams', 'classes','time-table', 'school-calendar'] 

ACADEMIC_FIELDS ={
    'subjects': ['code', 'name'],
    'e-notes': [],
    'exams': ['exam_name', 'exam_type'],
    'time-table': [],
    'school-calendar': [],
    'classes': ['form', 'stream']
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
    'school-calendar': {},
    'classes': {'form': 'Enter class level e.g 1'}

}

ACADEMIC_MODELS ={
    'subjects': SubjectsModel,
    'e-notes': ResourcesModel,
    'exams': ExamsModel,
    'time-table': None,
    'school-calendar': SchoolCalendarModel,
    'classes': ClassesModel
}

ACADEMIC_FORMS ={
    'subjects': SubjectForm,
    'e-notes': None,
    'exams': ExamForm,
    'time-table': None,
    'school-calendar': None,
    'classes': ClassForm
}