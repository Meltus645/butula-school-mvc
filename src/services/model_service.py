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
            try: order_key =self.model.order_key 
            except Exception: order_key ='' 
            if id: queryset:dict =self.model.objects.get(id=id)
            elif search_q: queryset:list =self.model.objects.search_text(search_q).order_by(order_key) 
            else: queryset:list =self.model.objects.filter(**filters).order_by(order_key) 
            response =queryset, 200

        except ValidationError as e:  response = { 'detail': 'cannot resolve params parsed' }, 400  
        except self.model.DoesNotExist: response ={'detail': 'not found'}, 404
        except Exception as e: response ={'detail': f'{e}'}, 500
        finally:  return response   
    
    def save(self, data:dict)->tuple:
        try:   
            new_item =self.model(**data).save() 
            # TODO: get some key value  
            response ={'detail': 'created successfully'}, 201 
        except FieldDoesNotExist as e:  response ={'detail': f'{e}'}, 400
        except DuplicateKeyError: response ={'detail': 'conflict'}, 409
        except NotUniqueError: response ={'detail': 'conflict'}, 409
        except ValidationError as e: response ={'detail': f'{e}'} , 400
        except Exception as e: response ={'detail': f'{e}'}, 500
        finally: return response

   
    def edit(self, id:str, data:dict)->tuple:
        try:
            for key in data.keys(): data[key] =self.model_refs(data[key])  
            print(data)
            self.model.objects.get(id=id).update(**data) 
            response =  {'detail': "changes saved successfully"}, 200 
        
        except self.model.DoesNotExist: response ={'detail': 'not found'}, 404
        except FieldDoesNotExist as e: response ={'detail': e.to_dict()}, 404
        except DuplicateKeyError: response = {'detail': 'conflict'}, 409
        except NotUniqueError: response = {'detail': 'conflict'}, 409
        except Exception as e: print(e)
        # except ValidationError as e: response ={'detail': f'invalid field {e.field_name}'}, 400 
        finally: return response

    
    def remove(self, id:str)->dict:
        try:
            self.model.objects.get(id=id).delete() 
            response ={'detail': []}, 204 
        except self.model.DoesNotExist: response ={'detail': 'ot found'}, 404 
        finally: return response
    
    def model_refs(self, ref)->dict: 
        if ObjectId.is_valid(ref): ref =ObjectId(oid=ref) 
        if type(ref) is list: ref =[self.model_refs(_ref) for _ref in ref]
        return ref