from mongoengine.errors import ValidationError, FieldDoesNotExist, NotUniqueError 
from pymongo.errors import DuplicateKeyError
from mongoengine import Document 
from bson.objectid import ObjectId 

class ModelService:
    """
        Performs crud operations on a model

        :param model -model to perform crud on
    """
    def __init__(self, model:Document) -> None:
        self.model =model

    def fetch(self, id:str =None, search_q:str =None, **filters)->tuple:
        try: 
            if id: queryset:dict =self.model.objects.get(id=id)
            elif search_q: queryset:list =self.model.objects.search_text(search_q) 
            else: queryset:list =self.model.objects.filter(**filters) 
            response =queryset, 200

        except ValidationError as e:  response = { 'detail': 'cannot resolve params parsed' }, 400  
        except self.model.DoesNotExist: response ={'detail': 'not found'}, 404
        except Exception as e: response ={'detail': f'{e}'}, 500
        finally:  return response   
    
    def save(self, data:dict)->tuple:
        try:  
            print(data)  
            new_item =self.model(**data).save() 
            response ={'detail': 'created successfully'}, 201 
        except FieldDoesNotExist as e:  response ={'detail': f'{e}'}, 400
        except DuplicateKeyError: response ={'detail': 'conflict'}, 409
        except NotUniqueError: response ={'detail': 'conflict'}, 409
        except ValidationError as e: response ={'detail': f'{e}'} , 400
        except Exception as e: response ={'detail': f'{e}'}, 500
        finally: return response

   
    def edit(self, id:str, data:dict)->tuple:
        try:
            for key in data.keys():
                if ObjectId.is_valid(oid=data[key]): data[key] =ObjectId(oid=data[key])

            self.model.objects.get(id=id).update(**data) 
            response =  {'detail': "changes saved successfully"}, 200 
        
        except self.model.DoesNotExist: response ={'detail': 'not found'}, 404
        except FieldDoesNotExist as e: response ={'detail': e.to_dict()}, 404
        except DuplicateKeyError: response = {'detail': 'conflict'}, 409
        except NotUniqueError: response = {'detail': 'conflict'}, 409
        except ValidationError as e:  
            response ={'detail': f'invalid field {e.field_name}'}, 400 
        finally: return response

    
    def remove(self, id:str)->dict:
        try:
            self.model.objects.get(id=id).delete() 
            response ={'detail': []}, 204 
        except self.model.DoesNotExist: response ={'detail': 'ot found'}, 404 
        finally: return response