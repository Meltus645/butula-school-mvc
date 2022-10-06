from flask_wtf import FlaskForm
from wtforms import StringField, DateField  

class CalendarForm(FlaskForm):
    year =StringField(label='year', name ='year', id ='year')
    term =StringField(label='Term', name ='term', id ='term')
    starts_from =DateField(label='Starts From', name ='starts_from', id ='starts_from')
    ends_on =DateField(label='Ends On', name ='ends_on', id ='ends_on')
      
    def __init__(self, data =None, **kwargs):
        super(CalendarForm, self).__init__(**kwargs) 
         
        if data: 
            self.year.default =data.year  
            self.term.default =data.term  
            self.starts_from.default =data.starts_from  
            self.ends_on.default =data.ends_on  
            self.process()
