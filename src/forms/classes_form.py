from flask_wtf import FlaskForm
from wtforms import StringField  

class ClassesForm(FlaskForm):
    form =StringField(label='Form', name ='form', id ='form')
    stream =StringField(label='Stream', name ='stream', id ='stream')
      
    def __init__(self, data =None, **kwargs):
        super(ClassesForm, self).__init__(**kwargs) 
         
        if data: 
            self.form.default =data.form  
            self.stream.default =data.stream  
            self.process()
