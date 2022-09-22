from flask import Blueprint
from src.controllers.admin_controller import dashboard 

admin =Blueprint('admin', __name__)

admin.route('/')(dashboard)