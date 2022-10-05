from .mediaWorker import MediaWorker

def upload_file(file, _type='img', swap_with:str =None)->tuple:
    worker = MediaWorker(file, _type) 
    if swap_with:
        done, filepath =worker.upload_media()
        if done: return worker.remove_media(swap_with) 
        return done, filepath
    return worker.upload_media() 