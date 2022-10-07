from werkzeug.utils import secure_filename
from uuid import uuid1  
import os, base64
from .exceptions import EmptyFileError, LargeFileError, UnSupportedFileError, UnreadableFileError

from .constants.app import BASEDIR

class MediaWorker: 
    def __init__(self, media, expected:str )->tuple: 
        self.media =media 
        self.allowed_metadata ={'img':  {'ext': ('png', 'jpg', 'jpeg'), 'mime': ('image/png', 'image/jpeg')}, 'doc': {'ext': ('pdf',), 'mime': ('application/pdf',)}, 'vid': {'ext': ('mp4',), 'mime': ('video',)}}
        self.filename =secure_filename(filename=self.media.filename).lower()
        self.expected_extensions =self.allowed_metadata[expected]['ext']
        self.expected_mimetypes  =self.allowed_metadata[expected]['mime']
        self.upload_dir =expected
        self.max_size =1024 *1024 
        self.media_root =BASEDIR /'media'  

    def upload_media(self, as_b64=False):
        try:  
            filename =self.validate_media() 
            if as_b64: return self.encode_media_to_base64()
            return self.save_media(filename=filename) 
        except Exception as e: return False, e
        
    def remove_media(self, file:str):
        try:    
            os.unlink(path=self.media_root /file)
            return True, None 
        except Exception as e: return False, f'{e}'

    def validate_media(self)->str:
        try:  
            self.blob  =self.media.read()   
            if len(self.blob) ==0: raise EmptyFileError() 
            file_extension =self.filename.split('.')[-1].strip() 
            mimetype =self.media.mimetype.lower()  
            if not file_extension in self.expected_extensions or not mimetype in self.expected_mimetypes: raise UnSupportedFileError(f"Only {','.join(self.expected_extensions)} are allowed.") # extension and 
            if len(self.blob) >self.max_size: raise LargeFileError("file larger than 1mb") 
            return self.filename
        except IOError: raise UnreadableFileError()

    def save_media(self, filename:str)->tuple: 
        try:  
            mediapath =f'{self.upload_dir}/{uuid1()}_{filename}' 
            # self.media.save(dst =self.media_root /mediapath)   
            with open(self.media_root /mediapath, 'wb') as fs: fs.write(self.blob)
            return True, mediapath
        except Exception as e: return False, f'{e}' 
    
    def encode_media_to_base64(self):
        try:   
            return True, base64.b64encode(self.blob).decode() 
        except Exception as e: False, f'{e}'