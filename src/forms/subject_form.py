from flask_wtf import FlaskForm
from wtforms import StringField  

class SubjectForm(FlaskForm):
    name =StringField(label='Name', name ='name', id ='name')
    code =StringField(label='Code', name ='code', id ='code')

    def __init__(self, data =None, **kwargs):
        super(SubjectForm, self).__init__(**kwargs) 
        if data: 
            self.name.default =data.name  
            self.code.default =data.code  
            self.process()
