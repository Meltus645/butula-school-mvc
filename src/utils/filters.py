import re, timeago 
from datetime import datetime

def slugify(url:str):
    if type(url) is str: return re.sub('\s+', '-', str(url).strip())
    elif type(url) is dict: return {list(url.keys())[0]: slugify(list(url.values())[0])}
    else: return url  

properties =lambda cls: dir(cls) # calls dir() on a class, cls
type_of =lambda obj: type(obj).__name__ 
strip_special =lambda text: re.sub('[_\W]+', ' ', str(text).strip())
since =lambda then: timeago.format(then, datetime.now()) # time difference between now and time_uploaded 