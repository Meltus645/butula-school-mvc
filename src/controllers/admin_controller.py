from flask import request, render_template, redirect, url_for, jsonify  
from .academic_service_controller import GET_ACADEMICS, POST_ACADEMICS, PUT_ACADEMICS, DELETE_ACADEMICS
from src.utils.constants.academics import ACADEMIC_FIELDS, ACADEMIC_FORMS, ACADEMIC_PLACEHOLDERS, ACADEMIC_SECTIONS 
from src.utils.constants.app import ACTIONS
from src.utils.constants.users import USER_FORMS, USER_TYPES
from flask_wtf import FlaskForm

def dashboard():
    return render_template('admin/base.html', page="dashboard")

def users(type:str, action='list', id =None, section:str ='bio'): 
    action =action.lower()
    type =type.lower() 
    params =request.args  
    form:FlaskForm =None 
    if not type in USER_TYPES or not action in ACTIONS: return redirect(url_for('admin.error_404'))
    
    if action == 'list':  
        if params.get('init') =='app': return render_template('list.html') 

    if action == 'new':  
        form =USER_FORMS[type]
        if params.get('init') =='app': return render_template('form.html', form =form) 

    if action == 'edit': 
        form =USER_FORMS[type]
        if params.get('init') =='app': return render_template('form.html', form =form) 

    if action == 'view':  
        if params.get('init') =='app': return render_template('view.html', section =section) 

    return render_template(f'{type}.html', page=type, action =action, form =form, section =section)

 
def academics(section ='e-notes', action ='list', id:str =None): 
    section =section.lower()
    action =action.lower() 
    if not section in ACADEMIC_SECTIONS or not action in ACTIONS: return redirect(url_for('admin.error_404'))
    
    params =request.args
    page ='academics' 
    data =None
    form: FlaskForm =ACADEMIC_FORMS[section] or None
    placeholders:dict =ACADEMIC_PLACEHOLDERS[section] or None
    fields =ACADEMIC_FIELDS[section] or None
     

    if action =='list': 
        data =GET_ACADEMICS[section]()   
        if params.get('init') =='app': return render_template('list.html', data=data, fields =fields, section =section, page =page, action =action)

    if action =='new':    
        if request.method =='POST':  return POST_ACADEMICS[section]()  
        if params.get('init') =='app': return render_template('form.html', form =form, section =section, page =page, action =action, placeholders =placeholders)

    if action =='edit':
        if request.method =='POST': return PUT_ACADEMICS[section](id=id)   
        data =GET_ACADEMICS[section](id=id)
        if params.get('init') =='app': 
            return render_template('form.html', form =form, section =section, page =page, action =action, placeholders =placeholders, data=data)

    if action =='view': 
        data =GET_ACADEMICS[section](id=id)
        if params.get('init') =='app': return render_template('list.html')

    if action == 'delete':
        response =DELETE_ACADEMICS[section](id=id)
        if response['detail'] ==204: return jsonify({'deleted': True})
        return jsonify({'deleted': False, 'detail': response['detail']})

    return render_template('academics.html', page =page, section =section, action =action, form =form, data =data, fields =fields, placeholders =placeholders)

def subscribers(): pass

def settings(): pass

def support(): pass 

def error_404():
    return render_template('404.html')

def error_403():
    return render_template('404.html')