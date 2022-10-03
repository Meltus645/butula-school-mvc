from src.models import ResourcesModel  
from flask_mongoengine.wtf import model_form

 

resource_form =model_form(
    model =ResourcesModel,
    exclude=[  
        'views',
        'downloads',
        'time_uploaded'
    ],
    field_args={
        'description': {
            'textarea': True
        }
    }
)
  