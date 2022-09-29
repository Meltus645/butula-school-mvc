from flask import request 
from mongoengine.errors import InvalidQueryError 
from src.services.exams_service import get_exam, post_exam, put_exam, delete_exam

def get(id:str =None)->tuple:
    try:  
        filters ={**request.args}
        if filters.get('init'): filters.pop('init')
        search_q =request.args.get('search_q')
        if id: return get_exam(id=id)
        elif search_q: response =get_exam(search_q=search_q)
        else: response =get_exam(**filters)  
        return  [exam.to_mongo() for exam in response]
    except ValueError: return {'detail': 'cannot resolve query params parsed'}, 400 
    except InvalidQueryError as e: return {'detail': 'cannot resolve query fields parsed'}, 400
    except Exception as e:  return {'detail': f'{e}'}, 500 
     
def post()->tuple:
    try: 
        data =request.get_json()
        data.pop('csrf_token')
        return post_exam(data) 
    except Exception as e: return {'detail': f'{e}'}, 500

def put(id:str)->tuple:
    try: 
        data =request.get_json()
        data.pop('csrf_token')
        return put_exam(id=id, data=data) 
    except Exception as e: return {'detail': f'{e}'}, 500 

def delete(id:str)->tuple:
    try: return delete_exam(id=id) 
    except Exception as e: return {'detail': f'{e}'}, 500 