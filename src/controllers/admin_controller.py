from flask import request, render_template, redirect, url_for
from src.services.students_service import get_sutudent, post_student, put_student, delete_student
from src.forms.studentsForm import StudentForm
from src.forms.staffForm import StaffForm
from flask_wtf import FlaskForm

def dashboard():
    return render_template('admin/base.html', page="dashboard")

def users(type:str, action='list', id =None, section:str ='bio'): 
    action =action.lower()
    type =type.lower() 
    params =request.args  
    form:FlaskForm =None
    forms:dict ={'students': StudentForm, 'staff': StaffForm}
    if not type in ['students', 'staff'] or not action in ['list', 'new', 'edit', 'view']: return redirect(url_for('admin.error_404'))
    
    if action == 'list':  
        if params.get('init') =='app': return render_template('list.html') 

    if action == 'new':  
        form =forms[type]
        if params.get('init') =='app': return render_template('form.html', form =form) 

    if action == 'edit': 
        form =forms[type]
        if params.get('init') =='app': return render_template('form.html', form =form) 

    if action == 'view':  
        if params.get('init') =='app': return render_template('view.html', page=type, section =section) 

    return render_template(f'{type}.html', page=type, action =action, form =form, section =section)

 
def academics(): pass

def settings(): pass

def support(): pass 

def error_404():
    return render_template('404.html')