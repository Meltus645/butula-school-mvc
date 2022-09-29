from src.controllers import subjects_controller as subject_service


GET_ACADEMICS ={
    'subjects': subject_service.get 
}

POST_ACADEMICS ={
    'subjects': subject_service.post 
}

PUT_ACADEMICS ={
    'subjects': subject_service.put 
}

DELETE_ACADEMICS ={
    'subjects': subject_service.delete 
}
 