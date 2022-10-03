from flask import Flask
from flask_mongoengine import MongoEngine
from flask_wtf import CSRFProtect 

from .utils.constants.app import BASEDIR
from .utils import load_filters
from .routes import admin, static, public

def create_app(test_config:dict =None):
     
    app =Flask(__name__, static_folder =BASEDIR /'assets', template_folder =BASEDIR /'templates')

    if test_config: app.config.from_mapping(test_config)
    else: app.config.from_pyfile(BASEDIR /'config.py') 

    CSRFProtect(app=app)
    MongoEngine(app=app)  

    load_filters(app=app)

    app.register_blueprint(admin, url_prefix ='/admin')   
    app.register_blueprint(static, url_prefix ='/')   
    app.register_blueprint(public, url_prefix ='/')      
    
    return app
 