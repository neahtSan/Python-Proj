from components.myPath import *

def check_input(input):
    if input.isnumeric():
        return f'input value cannot be numeric'
    if input.split()[0] not in ['help', 'view', 'get', 'put', 'quit']:
        return f'Wrong input order'
    return True

def check_file(fileName):
    if fileName in all_upload_file():
        return True
    return False