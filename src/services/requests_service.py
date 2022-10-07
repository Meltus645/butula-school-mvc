from flask import request, json 
from mongoengine import Document 
from .model_service import ModelService 
from mongoengine.errors import InvalidQueryError  
from werkzeug.utils import secure_filename 
from src.utils.passwords import generate_password, hash_password
from src.utils.constants.flags import Flags

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
            if not done: return result, 200 
            return self.model.save(result) 
        except Exception as e:  
            return {'detail': f'{e}'}, 500
    
    def put(self, id:str)->tuple: 
        try: 
            done, result =self.model_config(access_method ='put')
            if not done: return result

            return self.model.edit(id=id, data=result) 
        except Exception as e: 
            return {'detail': f'{e}'}, 500

    def delete(self, id:str)->tuple:
        try: return self.model.remove(id=id) 
        except Exception as e: return {'detail': f'{e}'}, 500 


    def model_config(self, access_method ='post')->tuple:
        form ={key: (json.loads(value) if len(value) >0 and (value[0]=='[' and value[-1] ==']') else value) for (key, value) in [*{**request.form}.items()]}  #  check if a value has [ at start and ] at end and decode it
        if form.get('csrf_token'): form.pop('csrf_token') 
        if 'birth_certificate_number' in form: form['password']  =hash_password(form.get('birth_certificate_number'))
        filekey =form.get('file_uploading') 
        if filekey: 
            file_received =request.files.get(filekey) 
            done, msg =upload_file(file_received, as_b64=True) 
            if done:  
                form['filename'] =secure_filename(file_received.filename)
                form[filekey] =msg 
            else:
                if access_method =='put':
                    if not msg.flag.name == Flags.FILE_EMPTY.name: return False, msg
            form.pop('file_uploading') 
        return True, form