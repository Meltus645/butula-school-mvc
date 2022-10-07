from sre_parse import FLAGS
from .constants.flags import Flags

class EmptyFileError(Exception):
    def __init__(self, message ='File is empty'):
        super(EmptyFileError, self).__init__(message)
        self.message =message
        self.flag =Flags.FILE_EMPTY

    def __str__(self) -> str:
        return self.message 

class LargeFileError(Exception):
    def __init__(self, message ='File too large'):
        super(LargeFileError, self).__init__(message)
        self.message =message
        self.flag =Flags.FILE_LARGE

    def __str__(self) -> str:
        return self.message 

class UnreadableFileError(IOError):
    def __init__(self,  message ='Error reading this file'):
        super(UnreadableFileError, self).__init__(message)
        self.message =message
        self.flag =Flags.FILE_UNREADABLE

    def __str__(self) -> str:
        return self.message 
        

class UnSupportedFileError(TypeError):
    def __init__(self, message ='Unsupported file format'):
        super(UnSupportedFileError, self).__init__(message)
        self.message =message
        self.flag =Flags.FILE_UNSUPPORTED

    def __str__(self) -> str:
        return self.message 
 