from src.models import StaffModel, StudentsModel
from src.forms import student_form, staff_form

USER_POSITIONS =['students', 'staff']

USER_FIELDS ={
    'students': ['name',  'admission_number', 'phone', 'form', 'status', 'enrolled'],
    'staff': ['name', 'staffid', 'gender', 'phone', 'role', 'status'], 
}

USER_PLACEHOLDERS ={
    'students': {
        'name': 'Enter first and last name',
        'admission_number': 'Enter admission number',
        'phone': 'Enter Parent/Guardian phone number',
        'birth_certificate_number': 'Enter student Birth certificate entry number' 
    },
    'staff': {
        'name': 'Enter first and last name',
        'staff_id': 'Enter staff Id',
        'phone': 'Enter phone number',
        'email': 'Enter an email address' 
    }
}

USER_FORMS ={
    'students': student_form,
    'staff': staff_form
}

USER_MODELS ={
    'students': StudentsModel,
    'staff': StaffModel
}