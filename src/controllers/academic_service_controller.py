from src.controllers import subjects_controller as subject_service
from src.controllers import exams_controller as exam_service


GET_ACADEMICS ={
    'subjects': subject_service.get, 
    'exams': exam_service.get
}

POST_ACADEMICS ={
    'subjects': subject_service.post,
    'exams': exam_service.post 
}

PUT_ACADEMICS ={
    'subjects': subject_service.put,
    'exams': exam_service.put 
}

DELETE_ACADEMICS ={
    'subjects': subject_service.delete,
    'exams': exam_service.delete 
}
 