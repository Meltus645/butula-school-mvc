from .mediaWorker import MediaWorker

def upload_file(file, _type='img', swap_with:str =None)->tuple:
    worker = MediaWorker(file, _type) 
    if swap_with:
        done, filepath =worker.upload(commit =False)
        if done: 
            done, new_path =worker.unload(swap_with, commit=False) 
            print(new_path)
            if done and new_path: return worker.commit(path=filepath, action='save')
            return {}, 200
            # return worker.revert()
        return done, filepath
    return worker.upload()
    