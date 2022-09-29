from src.models.examsModel import ExamsModel
from mongoengine.errors import ValidationError, FieldDoesNotExist, NotUniqueError 
from pymongo.errors import DuplicateKeyError

def get_exam(id:str=None, search_q:str =None, **filters)->dict:
    try: 

        if id: queryset:dict =ExamsModel.objects.get(id=id)
        elif search_q: queryset:list =ExamsModel.objects.search_text(search_q).order_by('exam_name')
        else: queryset:list =ExamsModel.objects.filter(**filters).order_by('exam_name')
        response =queryset

    except ValidationError as e:  response = { 'detail': 'cannot resolve params parsed' } 
    except ExamsModel.DoesNotExist: response ={'detail': 'exam missing. It could have been moved. Refresh this window and retry'}, 404
    except Exception as e: response ={'detail': f'{e}'} 
    finally:  return response 

def post_exam(data:dict)->tuple:  
    try:  
        new_exam =ExamsModel(**data).save() 
        response ={'detail': f'{new_exam.exam_name} exam created'}, 201 
    except FieldDoesNotExist as e:  response ={'detail': 'some fields are undefined'}, 400
    except DuplicateKeyError: response = {'detail': 'exam with name already exist. Check and try again'}, 409
    except NotUniqueError: response = {'detail': 'exam with name already exist. Check and try again'}, 409
    except ValidationError as e: response =e.to_dict() , 400
    finally: return response


def put_exam(id:str, data:dict)->tuple:
    try:
        ExamsModel.objects.get(id=id).update(**data) 
        response =  {'detail': f"changes made on {data['exam_name']} saved successfully"}, 200 
    
    except ExamsModel.DoesNotExist: response ={'detail': 'exam missing. It could have been moved. Refresh this window and retry'}, 404
    except FieldDoesNotExist as e: response ={'detail': e.to_dict()}, 404
    except DuplicateKeyError: response = {'detail': 'exam with name already exist. Check and try again'}, 409
    except ValidationError as e:   
        response ={'detail': f'invalid {e.field_name}'}, 400
    # except Exception as e:  
    #     response ={'detail': f'{e}'},500
    finally: return response

def delete_exam(id:str)->dict:
    try:
        ExamsModel.objects.get(id=id).delete() 
        response ={'detail': 204} 
    except ExamsModel.DoesNotExist: response ={'detail': 'exam missing. It could have been moved. Refresh this window and retry'}, 404
    finally: return response