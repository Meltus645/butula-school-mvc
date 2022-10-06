from flask_mongoengine.wtf import model_form   
from src.models import ClassesModel, ExamsModel, ResourcesModel, SchoolCalendarModel, SubjectsModel, TimetableModel
from src.forms import ResourceForm, TimetableForm, ExamForm, SubjectForm, ClassesForm, CalendarForm

ACADEMIC_SECTIONS =['e-notes', 'subjects', 'exams', 'classes','time-table', 'school-calendar'] 

ACADEMIC_FIELDS ={
    'subjects': ['code', 'name'],
    'e-notes': ['topic', 'subject', 'resource_type', 'author', 'views', 'downloads', 'time_uploaded'],
    'exams': ['exam_name', 'exam_type'],
    'time-table': ['form', 'purpose', 'filename'],
    'school-calendar': ['year', 'term', 'starts_from', 'ends_on'],
    'classes': ['form', 'stream']
}
 
ACADEMIC_PLACEHOLDERS ={
    'subjects': {
        'code': 'Enter subject code e.g 101',
        'name': 'Enter subject name e.g english'
    },
    'e-notes': {
        'topic': 'enter resource topic', 
        'description': 'Provide resource description or instructions'
    },
    'exams': {
        'exam_name': 'Enter Exam Name e.g C.A.T 1', 
    },
    'time-table': {},
    'school-calendar': {
        'year': 'Enter current academic year',
        'term': 'Enter current term'
    },
    'classes': {'form': 'Enter class level e.g 1', 'stream': 'Enter stream name'}

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
    'subjects': SubjectForm,
    'e-notes': ResourceForm,
    'exams': ExamForm,
    'time-table': TimetableForm,
    'school-calendar': CalendarForm,
    'classes': ClassesForm
}