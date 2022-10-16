from flask_wtf import FlaskForm 
from wtforms import HiddenField
from src.models.subjectsModel import SubjectsModel
import json

class SubjectsSelectionForm(FlaskForm):
    subjects =HiddenField(label='', name ='subjects_list', id ='subjects_list', render_kw ={'data-content': 'subjects'})
    def __init__(self, data =None, **kwargs):
        super(SubjectsSelectionForm, self).__init__(kwargs)
        self.subjects.render_kw['value'] =json.dumps([({'id': str(subject.id), 'name': subject.name, 'type': subject.subject_type, 'department': subject.department.name}) for subject in SubjectsModel.objects.all()])
        if data: 
            selected_subjects =[str(subject.id) for subject in data.subjects] 
            self.subjects.render_kw['value'] =json.dumps([{'id': str(subject.id), 'name': subject.name, 'selected': str(subject.id) in selected_subjects, 'type': subject.subject_type, 'department': subject.department.name} for subject in SubjectsModel.objects.all()])
            self.process()