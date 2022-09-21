from mongoengine import Document, StringField

class RolesModel(Document):
    name =StringField()

    meta ={'collection': 'role'}