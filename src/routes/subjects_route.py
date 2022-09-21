from flask import Blueprint
from src.controllers.subjects_controller import get, post, put, delete 

subjects_route =Blueprint('subjects_route', __name__)

subjects_route.route('/', methods =['GET'])(get)
subjects_route.route('/', methods =['POST'])(post) 
subjects_route.route('/<string:id>', methods =['GET'])(get)
subjects_route.route('/<string:id>', methods =['PUT'])(put)
subjects_route.route('/<string:id>', methods =['DELETE'])(delete)