from mongoengine import Document, StringField, ListField 

class ExamsModel(Document):
    exam_name =StringField(max_length=24)  #Buram, CAT 1
    exam_type =StringField(max_length=24)  #Internal, external
    schools =ListField(StringField(), required =True)
 
    meta ={'collection': 'exam', 'indexes': [{'fields': ['$exam_name', '$exam_type'], 'default_language': 'english'}]}