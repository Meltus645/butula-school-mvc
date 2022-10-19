from src.models import ExamsModel, ResourcesModel, SubjectsModel, GradeGroupModel, StaffModel, StudentsModel, ClassesModel, SchoolCalendarModel, TimetableModel, DepartmentsModel
from src.forms import ResourceForm, ExamForm, SubjectForm, GradeGroupForm, TimetableForm, ClassesForm, CalendarForm, DepartmentForm, StudentForm, StaffForm
 
FIELDS ={
    'dashboard': None,
    'academics': {
        'subjects': ['code', 'name', 'subject_type|type', 'department'],
        'e-notes': ['topic', 'subject', 'resource_type', 'author', 'time_uploaded'],
        'exams': ['exam_name', 'exam_type'], 
        'grading': []
    },
    'manage': { 
        'students': ['name',  'admission_number', 'phone', 'form', 'status', 'enrolled'],
        'staff': ['name', 'staff_id', 'gender', 'phone', 'role', 'status'],
    },
    'settings': {
        'time-table': ['form', 'purpose', 'filename'],
        'school-calendar': ['year', 'term', 'starts_from', 'ends_on'],
        'classes': ['form', 'stream'],
        'departments': ['name', 'head'],
    },  
    'support': None,
    'subscribers': None,
}

FORMS ={
    'dashboard': None,
    'academics': {
        'subjects': SubjectForm,
        'e-notes': ResourceForm,
        'exams': ExamForm, 
        'grading': GradeGroupForm,
    },
    'manage': { 
        'students': StudentForm,
        'staff': StaffForm,
    },
    'settings': {
        'time-table': TimetableForm,
        'school-calendar': CalendarForm,
        'classes': ClassesForm,
        'departments': DepartmentForm,
    },
    'support': None,
    'subscribers': None,
}

TEMPLATES ={
    'dashboard': 'base',
    'academics': 'academics',
    'manage': 'users',
    'settings': 'settings',
    'subscribers': 'subscribers',
    'support': 'support',
}

MODELS ={
    'dashboard': None,
    'academics': {
        'subjects': SubjectsModel,
        'e-notes': ResourcesModel,
        'exams': ExamsModel, 
        'grading': GradeGroupModel,
    },
    'manage': { 
        'students': StudentsModel,
        'staff':  StaffModel,
    },
    'settings': {
        'time-table': TimetableModel,
        'school-calendar': SchoolCalendarModel,
        'classes': ClassesModel,
        'departments': DepartmentsModel,
    },
    'support': None,
    'subscribers': None,
}

DEFAULT_SECTIONS ={
    'dashboard': None,
    'academics': 'e-notes', 
    'manage': 'students',
    'settings': 'school-calendar',
    'support': None,
    'subscribers': None,
}

SECTIONS ={
    'dashboard': None,
    'academics': ['e-notes', 'subjects', 'exams', 'grading'],
    'manage': ['staff', 'students'], 
    'settings': ['classes','time-table', 'school-calendar', 'departments', 'grades', 'carousels'],
    'support': None,
    'subscribers': None,
}

PLACEHOLDERS ={
    'dashboard': {},
    'academics': {
        'subjects': {
            'code': 'Enter subject code e.g 101',
            'name': 'Enter subject name e.g english' },
        'e-notes': {
            'topic': 'enter resource topic', 
            'description': 'Provide resource description or instructions' },
        'exams': {
            'exam_name': 'Enter Exam Name e.g C.A.T 1', }, 
        'grading': {},
    },
    'manage': {
        'students': {
            'name': 'Enter first and last name',
            'admission_number': 'Enter admission number',
            'phone': 'Enter Parent/Guardian phone number',
            'birth_certificate_number': 'Enter student Birth certificate entry number' },
        'staff': {
            'name': 'Enter first and last name',
            'staff_id': 'Enter staff Id',
            'phone': 'Enter phone number',
            'email': 'Enter an email address'}
    }, 
    'settings':{},
    'support': {},
    'subscribers': {},
}

FILE_MIMES ={ 
    'academics': {
        'time-table': 'application/pdf',
        'e-notes': 'application/pdf', 
    },
    'manage': '.png, .jpg, .jpeg'
}  