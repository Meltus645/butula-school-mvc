from flask import Blueprint
from src.controllers.public_controller import home

public =Blueprint('public', __name__) 

public.route('')(home)
public.route('index.html')(home)
public.route('home')(home)