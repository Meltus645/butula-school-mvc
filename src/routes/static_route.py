from flask import Blueprint
from src.controllers.static_controller import get_file

static =Blueprint('static', __name__)
 
static.route('favicon.png')(get_file)
static.route('favicon.ico')(get_file)
static.route('robots.txt')(get_file)
static.route('sitemap.xml')(get_file)