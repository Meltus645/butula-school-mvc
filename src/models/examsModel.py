from mongoengine import Document, StringField, ListField 

class ExamsModel(Document):
    exam_name =StringField(max_length=24, required =True, regex=r'[a-zA-Z]+[\. A-Za-z0-9]+', unique =True)  #Buram, CAT 1
    exam_type =StringField(max_length=24, required =True, regex=r'[a-zA-Z]+')  #Internal, external 
 
    meta ={'collection': 'exams', 'indexes': [{'fields': ['$exam_name', '$exam_type'], 'default_language': 'english'}]}