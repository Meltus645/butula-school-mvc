from flask import send_from_directory, current_app 
from src.utils.constants.app import BASEDIR

def get_file(path:str):   
    return send_from_directory(current_app.static_folder, path) 

def get_media(dir:str, path:str): 
    print(dir, path)
    return send_from_directory(BASEDIR, f'media/{dir}/{path}')