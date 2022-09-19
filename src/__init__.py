from flask import Flask
from flask_mongoengine import MongoEngine
from pathlib import Path

def create_app(test_config:dict =None):
    BASEDIR =Path(__file__).resolve().parent.parent 
    app =Flask(__name__, )

    if test_config: app.config.from_mapping(test_config)
    else: app.config.from_pyfile(BASEDIR / 'config.py')
    MongoEngine(app=app)

    return app
 