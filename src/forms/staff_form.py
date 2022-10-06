from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SelectField, EmailField
  
class StaffForm(FlaskForm):
    name =StringField(label='Name', name='name', id='name')
    staff_id =StringField(label='Staff ID', name= 'staff_id', id= 'staff_id')  
    phone =StringField(label='Phone', name= 'phone', id= 'phone')  
    email =EmailField(label='Email', name= 'email', id= 'email')  
    gender =SelectField(label='Gender', name ='gender', id ='gender', choices= [('', 'select gender'), ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    avatar =FileField(label='Passport Photo', name='avatar', id='avatar')

    def __init__(self, data =None, **kwargs):
        super(StaffForm, self).__init__(**kwargs)

        if data:
            self.name.default =data.name 
            self.staff_id.default =data.staff_id 
            self.phone.default =data.phone 
            self.email.default =data.email 
            self.gender.default =data.gender  

            self.process()