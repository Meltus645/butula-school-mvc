from .constants.admin import FIELDS, MODELS, FORMS, TEMPLATES, DEFAULT_SECTIONS, PLACEHOLDERS, FILE_MIMES
from .exceptions import PageNotFoundError

def get_leaf(data, key, section=None): 
    model =data.get(key)  
    if (model and type(model) is dict) and section:  return get_leaf(model, key =section)    
    return model 

def page_mapper(page:str, section:str)->tuple:  
    if not section: section =DEFAULT_SECTIONS[page] 
    try: 
        model ={
            'model': get_leaf(MODELS, page, section),
            'fields': get_leaf(FIELDS, page, section)
        } 
        form ={ 
            'form': get_leaf(FORMS, page, section),
            'placeholders': get_leaf(PLACEHOLDERS, page, section),
            'accepts': get_leaf(FILE_MIMES, page, section)
        }

        template ={
            'template': TEMPLATES.get(page),
            'section': section
        }
        return model, form, template
    except KeyError: raise PageNotFoundError