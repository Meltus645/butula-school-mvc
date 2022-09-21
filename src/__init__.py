from flask import Flask
from flask_mongoengine import MongoEngine
from pathlib import Path
from .routes import subjects

def create_app(test_config:dict =None):
    BASEDIR =Path(__file__).resolve().parent.parent 
    app =Flask(__name__, static_folder =BASEDIR /'assets', template_folder =BASEDIR /'templates')

    if test_config: app.config.from_mapping(test_config)
    else: app.config.from_pyfile(BASEDIR /'config.py')
    MongoEngine(app) 
    app.register_blueprint(subjects, url_prefix ='/subjects')   
    return app
 