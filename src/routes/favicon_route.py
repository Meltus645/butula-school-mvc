from flask import Blueprint
from src.controllers.favicon_controller import icon

favicon =Blueprint('favicon', __name__)
 
favicon.route('favicon.png')(icon)
favicon.route('favicon.ico')(icon)