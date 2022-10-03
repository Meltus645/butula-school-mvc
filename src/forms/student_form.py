from src.models import StudentsModel  
from flask_mongoengine.wtf import model_form

 

student_form =model_form(
    model =StudentsModel,
    exclude=[
        'subjects', 
        'status',
        'password',
        'gender',
        'enrolled'
    ]
)
         