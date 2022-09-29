from src.models.subjectsModel import SubjectsModel
from mongoengine.errors import ValidationError, FieldDoesNotExist, NotUniqueError 
from pymongo.errors import DuplicateKeyError

def get_subject(id:str=None, search_q:str =None, **filters)->dict:
    try: 

        if id: queryset:dict =SubjectsModel.objects.get(id=id)
        elif search_q: queryset:list =SubjectsModel.objects.search_text(search_q).order_by('code')
        else: queryset:list =SubjectsModel.objects.filter(**filters).order_by('code')
        response =queryset

    except ValidationError as e:  response = { 'detail': 'cannot resolve params parsed' } 
    except SubjectsModel.DoesNotExist: response ={'detail': 'subject missing. It could have been moved. Refresh this window and retry'}, 404
    except Exception as e: response ={'detail': f'{e}'} 
    finally:  return response 

def post_subject(data:dict)->tuple:  
    try:  
        new_subject =SubjectsModel(**data).save() 
        response ={'detail': f'{new_subject.name} subject created'}, 201 
    except FieldDoesNotExist as e:  response ={'detail': 'some fields are undefined'}, 400
    except DuplicateKeyError: response = {'detail': 'subject with code or name already exist. Check and try again'}, 409
    except NotUniqueError: response = {'detail': 'subject with code or name already exist. Check and try again'}, 409
    except ValidationError as e: response =e.to_dict() , 400
    finally: return response


def put_subject(id:str, data:dict)->tuple:
    try:
        SubjectsModel.objects.get(id=id).update(**data) 
        response =  {'detail': f"changes made on {data['name']} saved successfully"}, 200 
    
    except SubjectsModel.DoesNotExist: response ={'detail': 'subject missing. It could have been moved. Refresh this window and retry'}, 404
    except FieldDoesNotExist as e: response ={'detail': e.to_dict()}, 404
    except DuplicateKeyError: response = {'detail': 'subject with code or name already exist. Check and try again'}, 409
    except ValidationError as e:   
        response ={'detail': f'invalid {e.field_name}'}, 400
    # except Exception as e:  
    #     response ={'detail': f'{e}'},500
    finally: return response

def delete_subject(id:str)->dict:
    try:
        SubjectsModel.objects.get(id=id).delete() 
        response ={'detail': 204} 
    except SubjectsModel.DoesNotExist: response ={'detail': 'subject missing. It could have been moved. Refresh this window and retry'}, 404
    finally: return response