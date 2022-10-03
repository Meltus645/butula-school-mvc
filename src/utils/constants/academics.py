from flask_mongoengine.wtf import model_form   
from src.models import ClassesModel, ExamsModel, ResourcesModel, SchoolCalendarModel, SubjectsModel, TimetableModel
from src.forms import resource_form

ACADEMIC_SECTIONS =['e-notes', 'subjects', 'exams', 'classes','time-table', 'school-calendar'] 

ACADEMIC_FIELDS ={
    'subjects': ['code', 'name'],
    'e-notes': ['topic', 'subject', 'views', 'downloads', 'author', 'time_uploaded'],
    'exams': ['exam_name', 'exam_type'],
    'time-table': ['form', 'purpose', 'file'],
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
    'time-table': TimetableModel,
    'school-calendar': SchoolCalendarModel,
    'classes': ClassesModel
}

ACADEMIC_FORMS ={
    'subjects': model_form(SubjectsModel),
    'e-notes': resource_form,
    'exams': model_form(ExamsModel),
    'time-table': model_form(TimetableModel),
    'school-calendar': model_form(SchoolCalendarModel),
    'classes': model_form(ClassesModel)
}