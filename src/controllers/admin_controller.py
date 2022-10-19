from wtforms import FloatField 
from flask import request, render_template, jsonify   
from src.forms import ResultsForm, SubjectsSelectionForm
from src.services.requests_service import RequestsService 
from src.utils.exceptions import PageNotFoundError 
from src.utils.constants.app import ACTIONS 
from src.utils.mappers import page_mapper

def controller(page ='dashboard', section:str =None, action:str =None, id:str =None):
    try: 
        if not action: action ='list'
        if not action in ACTIONS: raise PageNotFoundError
        model_data, form_data, template_data =page_mapper(page =page, section =section) 
        service =RequestsService(model=model_data.get('model'))
        fields =model_data.get('fields') 
        form =form_data.get('form') 
        placeholders:dict =form_data.get('placeholders') 
        accepts:list =form_data.get('accepts')
        template =template_data.get('template')
        section =template_data.get('section')
        params =request.args
        data =None 
        tab =params.get('tab')
        if page =='manage' and not tab in ['subjects', 'performance']: tab ='bio' 
        context ={'page': page, 'section': section, 'action': action, 'tab': tab} 

        if action =='list': 
            data, status_code =service.get()   
            context ={**context, 'data': data, 'fields': fields}
            if params.get('init') =='app': return render_template('list.html', **context)

        if action =='new':    
            if request.method =='POST': return service.post() 
            context ={**context, 'form': form, 'placeholders': placeholders, 'accepts': accepts}
            if params.get('init') =='app': return render_template('form.html', **context)

        if action =='edit':
            if request.method =='POST': return service.put(id=id)    
            data, _ =service.get(id=id)
            context ={**context, 'form': form, 'placeholders': placeholders, 'accepts': accepts, 'data': data}
            if params.get('init') =='app': return render_template('form.html', **context)

        if action == 'view':  
            data, _ =service.get(id=id) 
            popup = params.get('popup') 
            context ={**context, 'data': data}
            field = section
            if page =='manage': field =tab 
            if request.method =='POST': return service.put(id =id, data={field: request.form.get(field)}) 
            if popup:
                if tab == 'performance':
                    form =ResultsForm
                    for subject in data.subjects: setattr(form, subject.name.lower(), FloatField(label=subject.name, name =f'{subject.code}'))
                elif tab =='subjects': form =SubjectsSelectionForm  
                context ={**context, 'data': data, 'popup': popup, 'form': form, 'placeholders': placeholders,'accepts': accepts}
                return render_template('modal.html', **context)
            if params.get('init') =='app': return render_template('view.html', **context)

        if action == 'delete':
            response, status_code =service.delete(id=id)
            if status_code ==204: return jsonify({'deleted': True})
            return jsonify({'deleted': False, 'detail': response.get('detail')})
        
        return render_template(f'admin/{template}.html', **context)
    except PageNotFoundError: return {'page': 'Not Found'} 