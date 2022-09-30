from flask import request 
from mongoengine import Document 
from .model_service import ModelService
from mongoengine.errors import InvalidQueryError 

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
            return  [resp.to_mongo() for resp in response], status_code
        except ValueError: return {'detail': 'cannot resolve query params parsed'}, 400 
        except InvalidQueryError as e: return {'detail': 'cannot resolve query fields parsed'}, 400
        except Exception as e:  return {'detail': f'{e}'}, 500 
    
    def post(self)->tuple:
        try: 
            data =request.get_json()
            data.pop('csrf_token')
            return self.model.save(data) 
        except Exception as e: return {'detail': f'{e}'}, 500
    
    def put(self, id:str)->tuple:
        try: 
            data =request.get_json()
            data.pop('csrf_token')
            return self.model.edit(id=id, data=data) 
        except Exception as e: return {'detail': f'{e}'}, 500

    def delete(self, id:str)->tuple:
        try: return self.model.remove(id=id) 
        except Exception as e: return {'detail': f'{e}'}, 500 