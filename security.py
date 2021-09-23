#from werkzeug.security import safe_str_cmp #for python 2.7
'''
import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)
'''

from models.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    #if user and safe_str_cmp(user.password == password): for python 2.7
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)