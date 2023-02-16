from components.myPath import *

#check_input function return if the input form user is valid or not (take 1 parameter, input)
def check_input(input):
    if input == '':
        return f'input cannot be empty string!'
    if input.isnumeric():
        return f'input value cannot be numeric'
    if input.split()[0] not in ['help', 'newuser', 'login', 'share', 'logout','view', 'get', 'put', 'quit']:
        return f'Wrong input order'
    return True

#check_file return if the upload fileName is in upload directory or not (take 1 parameter, fileName) 
def check_file(fileName):
    if fileName in all_upload_file():
        return True
    return False