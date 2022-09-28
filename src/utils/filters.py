import re

def slugify(url:str):
    if type(url) is str: return re.sub('\s+', '-', str(url).strip())
    elif type(url) is dict: return {list(url.keys())[0]: slugify(list(url.values())[0])}
    else: return url 