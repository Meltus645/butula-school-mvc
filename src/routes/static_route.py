from flask import Blueprint
from src.controllers.static_controller import get_file, get_media

static =Blueprint('static', __name__)
 
static.route('/media/<string:dir>/<string:path>')(get_media)
static.route('<string:path>')(get_file) 