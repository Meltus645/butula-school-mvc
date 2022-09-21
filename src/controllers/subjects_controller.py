from flask import request, jsonify
from mongoengine.errors import InvalidQueryError, LookUpError
from src.services.subjects_service import get_subjects, post_subject, put_subject, delete_subject

def get(id:str =None)->dict:
    try:  
        search_q =request.args.get('search_q')
        if id: response, status_code =get_subjects(id=id)
        elif search_q: response, status_code =get_subjects(search_q=search_q)
        else: response, status_code =get_subjects(**request.args) 
        return  jsonify(response), status_code 
    except ValueError: return jsonify({'detail': 'cannot resolve query params parsed'}), 400 
    except InvalidQueryError as e: return jsonify({'detail': 'cannot resolve query fields parsed'}), 400
    except Exception as e:  return jsonify({'detail': f'{e}'}), 500 
     
def post()->dict:
    try:
        response, status_code =post_subject(request.get_json())  
        return jsonify(response), status_code
    except Exception as e: return jsonify({'detail': f'{e}'}), 500

def put(id:str)->dict:
    try:
        response, status_code =put_subject(id=id, data=request.get_json())
        return jsonify(response), status_code
    except Exception as e: return jsonify({'detail': f'{e}'}), 500 

def delete(id:str)->dict:
    try:
        response, status_code =delete_subject(id=id)
        return jsonify(response), status_code
    except Exception as e: return jsonify({'detail': f'{e}'}), 500 