from flask import request 
from mongoengine import Document 
from .model_service import ModelService 
from mongoengine.errors import InvalidQueryError  

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
            form ={**request.form}   
            if form.get('csrf_token'): form.pop('csrf_token') 
            filekey =form.get('file_uploading')
            if filekey: 
                done, filepath =upload_file(request.files.get(filekey)) 
                if done:  form[filekey] =filepath 
                else: return filepath, 500 
                form.pop('file_uploading') 
            return self.model.save(form) 
        except Exception as e: return {'detail': f'{e}'}, 500
    
    def put(self, id:str)->tuple: 
        try: 
            form ={**request.form}   
            if form.get('csrf_token'): form.pop('csrf_token')
            filekey, prev_path =[item.strip() for item in form.get('file_uploading').split('&')]  
            if filekey:  
                done, filepath =upload_file(request.files.get(filekey), swap_with =prev_path) 
                if done:  form[filekey] =filepath 
                else: 
                    print(filepath)
                form.pop('file_uploading') 
                return {}, 200
            # return self.model.edit(id=id, data=form) 
        except Exception as e: 
            return {'detail': f'{e}'}, 500

    def delete(self, id:str)->tuple:
        try: return self.model.remove(id=id) 
        except Exception as e: return {'detail': f'{e}'}, 500 
