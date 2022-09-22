from flask import request, render_template
from src.services.students_service import get_sutudent, post_student, put_student, delete_student

def dashboard():
    return render_template('admin/base.html')

def users(): 
    pass
 
def academics(): pass

def settings(): pass

def support(): pass 