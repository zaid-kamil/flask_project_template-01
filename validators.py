'''
file that contains helper functions for validation
of username, email, password, etc.
'''

import re

def validate_username(username):
    '''validate username'''
    if len(username) < 3:
        return False
    return True

def validate_email(email):
    '''validate email'''
    if len(email) < 7:
        return False
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    return True

def validate_password(password):
    '''validate password'''
    if len(password) < 6:
        return False
    return True

def validate_city(city):
    '''validate city'''
    if len(city) < 2:
        return False
    return True

def validate_avatar(file):
    '''validate avatar'''
    name, ext = file.filename.split('.')
    if file.filename == '':
        return False
    if ext not in ['jpg', 'jpeg', 'png', 'gif']:
        return False
    return True
