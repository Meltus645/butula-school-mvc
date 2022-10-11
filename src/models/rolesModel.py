from mongoengine import Document, StringField

class RolesModel(Document):
    name =StringField()

    meta ={'collection': 'role'}
    def __str__(self): return f'{self.name}'