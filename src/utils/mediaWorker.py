from werkzeug.utils import secure_filename
from uuid import uuid1  
import os
import shutil

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
        self.history =[]  

    def upload(self, commit =True):
        try:  
            filename =self.validate_media()  
            return self.save_media(filename=filename, commit=commit) 
        except Exception as e: return False, f'{e}'
        
    def unload(self, path:str, commit =True):
        try:
            self.src =f'{self.media_root /path}'
            self.dst =f"{self.media_root / 'tmp' /'_'.join(path.split('/'))}" 
            if not commit:  return self.move(src=self.src, dst=self.dst)  
            os.unlink(path=self.src)
            return True, None 
        except Exception as e: return False, f'{e}'

    def validate_media(self)->str: 
        filename =secure_filename(filename=self.media.filename).lower() 
        file_extension =filename.split('.')[-1].strip() 
        mimetype =self.media.mimetype.lower()  
        if not file_extension in self.expected_extensions or not mimetype in self.expected_mimetypes: raise TypeError(f"Only {','.join(self.expected_extensions)} are allowed.") # extension and 
        elif len(self.media.read()) >self.max_size: raise ValueError("413: file larger than 1mb") 
        return filename

    def save_media(self, filename:str, commit =True)->tuple: 
        try: 
            if not commit:  
                mediapath =f'tmp/{self.upload_dir}_{uuid1()}_{filename}'
                self.media.save(f"{self.media_root}/{mediapath}")
                return True, mediapath

            mediapath =f'{self.upload_dir}/{uuid1()}_{filename}'
            self.media.save(f"{self.media_root}/{mediapath}")
            self.media.close()
            return True, mediapath
        except Exception as e: return False, f'{e}'
    
    def commit(self, path:str, action ='save'):
        if not action in ['save', 'delete']: return False, 'action not allowed'
        if action =='delete': pass
        print(path)
        # self.move() 
        # self.media.close() 
    
    def revert(self, history): pass

    def move(self, src:str, dst:str):
        try:  
            return True, shutil.move(src=src, dst=dst)
        except Exception as e: return False, f'{e}'