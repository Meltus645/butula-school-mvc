from flask import Flask
from flask_mongoengine import MongoEngine
from flask_wtf import CSRFProtect

from .utils.constants import BASEDIR
from .routes import subjects, admin, static, public

def create_app(test_config:dict =None):
     
    app =Flask(__name__, static_folder =BASEDIR /'assets', template_folder =BASEDIR /'templates')

    if test_config: app.config.from_mapping(test_config)
    else: app.config.from_pyfile(BASEDIR /'config.py') 

    CSRFProtect(app=app)
    MongoEngine(app=app) 

    app.register_blueprint(static, url_prefix ='/')   
    app.register_blueprint(public, url_prefix ='/')   
    app.register_blueprint(subjects, url_prefix ='/subjects')   
    app.register_blueprint(admin, url_prefix ='/admin')   
    
    return app
 