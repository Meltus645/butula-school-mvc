from hashlib import sha256
from random import choices
 
generate_password = lambda : ''.join(choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-*/().+=@#%&%", k=12))
hash_password = lambda password: sha256(string=password.encode()).hexdigest() 