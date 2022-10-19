from flask import Blueprint
from src.utils.constants.app import BASEDIR

from src.controllers.public_controller import home, library, admissions, about, contacts, subscribe, policy, portal 

public =Blueprint('public', __name__) 

public.route('')(home) 
public.route('/library')(library) 
public.route('/admissions')(admissions) 
public.route('/portal')(portal) 
public.route('/about')(about) 
public.route('/contacts')(contacts) 
public.route('/subscribe', methods =['POST'])(subscribe) 
public.route('/privacy-policy')(policy)  
