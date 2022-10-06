from flask import request, render_template, redirect, url_for, jsonify   
from src.utils.constants.academics import ACADEMIC_FIELDS, ACADEMIC_FORMS, ACADEMIC_PLACEHOLDERS, ACADEMIC_SECTIONS, ACADEMIC_MODELS 
from src.utils.constants.app import ACTIONS
from src.utils.constants.users import USER_FORMS, USER_MODELS, USER_POSITIONS, USER_PLACEHOLDERS, USER_FIELDS
from src.services.requests_service import RequestsService
from flask_wtf import FlaskForm


def dashboard():
    return render_template('admin/base.html', page="dashboard")

def users(position:str, action='list', id =None, section:str ='bio'): 
    action =action.lower()
    position =position.lower() 
    if not position in USER_POSITIONS or not action in ACTIONS: return redirect(url_for('admin.error_404')), 404

    model =USER_MODELS[position]
    service =RequestsService(model=model)
    params =request.args  
    form:FlaskForm =None 
    data: dict =None
    page =position
    
    
    if action == 'list':  
        data, status_code =service.get()
        if params.get('init') =='app': return render_template('list.html', fields =USER_FIELDS[position], data=data, page=page, position=position), status_code 

    if action == 'new':  
        if request.method =='POST':  
            response, status_code =service.post()
            return response 
        form =USER_FORMS[position] 
        if params.get('init') =='app': return render_template('form.html', form =form, placeholders =USER_PLACEHOLDERS[position], page=page) 

    if action == 'edit': 
        if request.method =='POST': 
            response, status_code =service.put(id=id)

        data, status_code =service.get(id=id)    
        form =USER_FORMS[position]
        if params.get('init') =='app': return render_template('form.html', form =form, placeholders =USER_PLACEHOLDERS[position], page =page) 

    if action == 'view':  
        data, status_code =service.get(id=id)    
        if params.get('init') =='app': return render_template('view.html', section =section, data =data, page =page) 

    return render_template(f'{position}.html', page=page, action =action, form =form, section =section, placeholders =USER_PLACEHOLDERS[position], fields =USER_FIELDS[position], data =data)

 
def academics(section ='e-notes', action ='list', id:str =None): 
    section =section.lower()
    action =action.lower() 
    if not section in ACADEMIC_SECTIONS or not action in ACTIONS: return redirect(url_for('admin.error_404'))

    model =ACADEMIC_MODELS[section]
    service =RequestsService(model=model)
    params =request.args
    page ='academics' 
    data =None
    form: FlaskForm =ACADEMIC_FORMS[section] or None
    placeholders:dict =ACADEMIC_PLACEHOLDERS[section] or None
    fields =ACADEMIC_FIELDS[section] or None
     

    if action =='list': 
        data, status_code =service.get()   
        if params.get('init') =='app': return render_template('list.html', data=data, fields =fields, section =section, page =page, action =action)

    if action =='new':    
        if request.method =='POST':  
            response, status_code =service.post()
            return response 
        if params.get('init') =='app': return render_template('form.html', form =form, section =section, page =page, action =action, placeholders =placeholders)

    if action =='edit':
        if request.method =='POST': 
            response, status_code =service.put(id=id) 
            return response   

        data, status_code =service.get(id=id)
        if params.get('init') =='app': 
            return render_template('form.html', form =form, section =section, page =page, action =action, placeholders =placeholders, data=data)

    if action =='view': 
        data, status_code =service.get(id=id)
        if params.get('init') =='app': return render_template('list.html')

    if action == 'delete':
        response, status_code =service.delete(id=id)
        if status_code ==204: return jsonify({'deleted': True})
        return jsonify({'deleted': False, 'detail': response['detail']})
     
    return render_template('academics.html', page =page, section =section, action =action, form =form, data =data, fields =fields, placeholders =placeholders)

def subscribers(): 
    page  ='subscribers'
    return render_template('maillist.html', page=page)

def support(): 
    page  ='support'
    return render_template('support.html', page=page) 

def settings(): 
    page  ='settings'
    return render_template('settings.html', page=page)

def error_404():
    return render_template('404.html')

def error_403():
    return render_template('404.html')