from flask import send_from_directory, current_app, request

def get_file():  
    return send_from_directory(current_app.static_folder, request.path[1:]) 