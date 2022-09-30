from flask import render_template, request 
from src.models import TicketsModel
from flask_mongoengine.wtf import model_form


def home(): 
    return render_template('public/base.html')

def portal(): 
    return  {}

def library(): 
    return render_template('public/library.html')

def admissions(): 
    return render_template('public/admissions.html')

def about(): 
    return render_template('public/about.html')

def contacts(): 
    if request.method =='POST': pass 
   
    return render_template('public/contacts.html',  form =model_form(TicketsModel))

def subscribe(): 
    return {} 

def policy(): 
    return render_template('public/policy.html')

def terms(): 
    return render_template('public/terms.html')