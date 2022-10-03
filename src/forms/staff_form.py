from src.models import StaffModel 
from flask_mongoengine.wtf import model_form

 

staff_form =model_form(
    model =StaffModel,
    exclude=[  
        'status',
        'permissions',
        'role',
        'group',
        'otp',
        'password', 
        'email_verified',
        'created'  
    ]
)
  