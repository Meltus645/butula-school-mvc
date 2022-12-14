from flask import request, json 
from mongoengine import Document 
from .model_service import ModelService 
from mongoengine.errors import InvalidQueryError  
from werkzeug.utils import secure_filename 
from src.utils.passwords import generate_password, hash_password
from src.utils.constants.flags import Flags 
from src.models.subjectsModel import SubjectsModel

from src.utils.file_upload import upload_file

class RequestsService:
    def __init__(self, model:Document, **kwargs):
        self.model =ModelService(model=model)

    def get(self, id:str =None)->tuple:
        try:  
            filters ={**request.args}
            if filters.get('init'): filters.pop('init')
            search_q =request.args.get('search_q')
            if id: return self.model.fetch(id=id)
            elif search_q: response,status_code =self.model.fetch(search_q=search_q)
            else: response,status_code =self.model.fetch(**filters)  
            return  [resp for resp in response], status_code
        except ValueError: return {'detail': 'cannot resolve query params parsed'}, 400 
        except InvalidQueryError as e: return {'detail': 'cannot resolve query fields parsed'}, 400
        except Exception as e:  return {'detail': f'{e}'}, 500 
    
    def post(self)->tuple:
        try:  
            done, result =self.model_config() 
            if not done: return result, 400 
            return self.model.save(result) 
        except Exception as e:  
            return {'detail': f'{e}'}, 400
    
    def put(self, id:str, data=None)->tuple: 
        try: 
            done, result =self.model_config(access_method ='put', data=data)
            print(result)
            if not done: return result

            return self.model.edit(id=id, data=result) 
        except Exception as e: 
            return {'detail': f'{e}'}, 400

    def delete(self, id:str)->tuple:
        try: return self.model.remove(id=id) 
        except Exception as e: return {'detail': f'{e}'}, 500 


    def model_config(self, access_method ='post', data =None)->tuple:
        if data: request_form =data
        else: request_form =request.form
        form ={key: (json.loads(value) if len(value) >0 and (value[0]=='[' and value[-1] ==']') else value) for (key, value) in [*{**request_form}.items()]}  #  check if a value has [ at start and ] at end and decode it
        if access_method =='post' and 'student_subjects' in form: 
            form.pop('student_subjects') 
            form['subjects'] =[subject.id for subject in SubjectsModel.objects.filter(subject_type ='Compulsory')]
        if form.get('csrf_token'): form.pop('csrf_token') 
        filekey =form.get('file_uploading') 
        empty ={key: f'{key} required*'.replace('_', ' ').capitalize() for (key, value) in [*{**form}.items()] if len(value) <=0}
        if len(empty) >0: return False, empty
        if 'birth_certificate_number' in form: form['password']  =hash_password(form.get('birth_certificate_number'))
        if 'staff_id' in form: form['password'] =hash_password(generate_password()) 
        if filekey: 
            file_received =request.files.get(filekey) 
            done, msg =upload_file(file_received, as_b64=True) 
            if done:  
                form['filename'] =secure_filename(file_received.filename)
                form[filekey] =msg 
            else: 
                if access_method =='put':
                    if not msg.flag.name == Flags.FILE_EMPTY.name: return False, msg
                    else: return False, msg
            form.pop('file_uploading') 
        return True, form