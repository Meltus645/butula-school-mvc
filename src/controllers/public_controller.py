from flask import render_template, request 
from src.models import TicketsModel
from flask_mongoengine.wtf import model_form


def home(): 
    context ={
        'macros': [
            "Butula National School. Home of champions",
            "Top performing national boys' school located in Busia County.",
            ['Butula', 'School', 'Busia', 'National Schools', 'Boy Schools', 'Busia County', 'Best Schools'],
            "public.home"
        ] 
    }
    return render_template("public/base.html", **context)

def portal(): 
    return  {}

def library(): 
    context ={
        'macros': [
            "Butula School - Library",
            "Online School libray. Students can access all study resources even if out of school",
            ['Butula', 'School', 'Busia', 'National Schools', 'Boy Schools', 'Busia County', 'Best Schools', 'Library', 'academics', 'research', 'school library', 'butula school libray'],
            "public.library"
        ] 
    }
    return render_template("public/library.html", **context)

def admissions(): 
    context ={
        'macros': [
            "Butula School - New Student admissions",
            "The best school for your child",
            ['Butula', 'School', 'Busia', 'National Schools', 'Boy Schools', 'Busia County', 'Best Schools', 'Student admissions', 'form one', 'enroll student'],
            "public.admissions"
        ] 
    }
    return render_template("public/admissions.html", **context)

def about(): 
    context ={
        'macros': [
            "Butula School- About our school",
            "Our story, motto, vision, mission,achievements, facilities as a school",
            ['Butula', 'School', 'Busia', 'National' 'Schools', 'Boy Schools', 'Busia County', 'Best Schools', 'about butula school', 'school motto', 'school vision', 'school mission', 'school achievements', 'school faq'],
            "public.about"
        ] 
    }
    return render_template("public/about.html", **context)

def contacts(): 
    context ={
        'macros': [
            "Butula School - Contacts information",
            "The Official Butula School communication channel links",
            ['Butula', 'School', 'Busia', 'National Schools', 'Boy Schools', 'Busia County', 'Best Schools', 'contact butula boys', 'get in touch with butula boys', 'butula boys communication', 'Butula school customer care'],
            "public.contacts"
        ] 
    }
    if request.method =="POST": pass 
    return render_template("public/contacts.html",  form =model_form(TicketsModel), **context)

def subscribe(): 
    return {} 

def policy(): 
    context ={
        'macros': [
            "Butula School. User data consent and privacy Policy",
            "Butula School user data collection, storage, and usage consent document. We do not share your information whatsoever. Learn how We do it.",
            ['Butula', 'School', 'Busia', 'National Schools', 'Boy Schools', 'Busia County', 'Best Schools', 'Privacy Policy', 'User data', 'User Privacy consent'],
            "public.policy"
        ] 
    }
    return render_template("public/policy.html", **context)
