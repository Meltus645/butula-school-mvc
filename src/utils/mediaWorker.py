from werkzeug.utils import secure_filename
from uuid import uuid1  
import os 

from .constants.app import BASEDIR

class MediaWorker: 
    def __init__(self, media, expected:str )->tuple: 
        self.media =media 
        self.allowed_metadata ={'img':  {'ext': ('png', 'jpg', 'jpeg'), 'mime': ('image/png', 'image/jpeg', 'image/jpg')}, 'doc': {'ext': ('pdf',), 'mime': ('application',)}, 'vid': {'ext': ('mp4',), 'mime': ('video',)}}
        
        self.expected_extensions =self.allowed_metadata[expected]['ext']
        self.expected_mimetypes  =self.allowed_metadata[expected]['mime']
        self.upload_dir =expected
        self.max_size =1024 *1024 
        self.media_root =BASEDIR /'media'   

    def upload_media(self):
        try:  
            filename =self.validate_media()  
            return self.save_media(filename=filename) 
        except Exception as e: return False, f'{e}'
        
    def remove_media(self, file:str):
        try:    
            os.unlink(path=self.media_root /file)
            return True, None 
        except Exception as e: return False, f'{e}'

    def validate_media(self)->str: 
        filename =secure_filename(filename=self.media.filename).lower() 
        file_extension =filename.split('.')[-1].strip() 
        mimetype =self.media.mimetype.lower()  
        if not file_extension in self.expected_extensions or not mimetype in self.expected_mimetypes: raise TypeError(f"Only {','.join(self.expected_extensions)} are allowed.") # extension and 
        # elif len(self.media.read()) >self.max_size: raise ValueError("413: file larger than 1mb") 
        return filename

    def save_media(self, filename:str)->tuple: 
        try:  
            mediapath =f'{self.upload_dir}/{uuid1()}_{filename}' 
            self.media.save(dst =self.media_root /mediapath)   
            return True, mediapath
        except Exception as e: return False, f'{e}' 