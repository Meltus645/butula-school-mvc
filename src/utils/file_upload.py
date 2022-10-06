from .mediaWorker import MediaWorker

def upload_file(file, _type='img', swap_with:str =None, as_b64 =False)->tuple:
    worker = MediaWorker(file, _type)  
    if swap_with:
        done, filepath =worker.upload_media(as_b64 =as_b64)
        if done: return worker.remove_media(swap_with) 
        return done, filepath
    return worker.upload_media(as_b64 =as_b64)  
