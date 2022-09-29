from flask import request
from mongoengine.errors import ValidationError, FieldDoesNotExist, NotUniqueError 
from pymongo.errors import DuplicateKeyError
from src.models.studentsModel import StudentsModel

def get_student(id:str=None, search_q:str =None, **filters)->tuple:
    try: 
        if id: queryset:dict =StudentsModel.objects.get(id=id)
        elif search_q: queryset:list =StudentsModel.objects.search_text(search_q).order_by('name')
        else: queryset:list =StudentsModel.objects.filter(**filters).order_by('name')
        response ={'data': queryset}, 200
    except ValidationError as e:  response = { 'detail': 'cannot resolve params parsed' }, 400  
    except StudentsModel.DoesNotExist: response ={'detail': 'student missing. He could have been moved. Refresh this window and retry'}, 404
    except Exception as e: response ={'detail': f'{e}'}, 500
    finally:  return response 

def post_student(data:dict)->tuple:  
    try:  
        # save image if available and url as avatar, encrypt birth no. and save to password
        new_Student =StudentsModel(**data).save() 
        response ={'detail': f'{new_Student.name} was created successfully'}, 201 
    except FieldDoesNotExist as e:  response ={'detail': 'some fields are undefined'}, 400
    except DuplicateKeyError: response = {'detail': 'student with admission or birth certificate number  already exist. Check and try again'}, 409
    except NotUniqueError: response = {'detail': 'student with admission or birth certificate number  already exist. Check and try again'}, 409
    except ValidationError as e: response =e.to_dict() , 400
    finally: return response


def put_student(id:str, data:dict)->tuple:
    try:
        StudentsModel.objects.get(id=id).update(**data) 
        response =  {'detail': f"changes made on {data['name']} saved successfully"}, 200 
    
    except StudentsModel.DoesNotExist: response ={'detail': 'student missing. He could have been moved. Refresh this window and retry'}, 404
    except FieldDoesNotExist as e: response ={'detail': e.to_dict()}, 404
    except DuplicateKeyError: response = {'detail': 'student with admission or birth certificate number  already exist. Check and try again'}, 409
    except NotUniqueError: response = {'detail': 'student with admission or birth certificate number  already exist. Check and try again'}, 409
    except ValidationError as e:   
        response ={'detail': f'invalid {e.field_name}'}, 400
    # except Exception as e:  
    #     response ={'detail': f'{e}'},500
    finally: return response

def delete_student(id:str)->tuple:
    try:
        StudentsModel.objects.get(id=id).delete() 
        response ={'detail': 'student removed successfully' }, 204
    except StudentsModel.DoesNotExist: response ={'detail': 'student missing. He could have been moved. Refresh this window and retry'}, 404
    finally: return response