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

def check_newuser_format(rawInput):
    if len(rawInput.split()) != 4:
        return f'wrong format for crate user please input >> newuser [username] [password] [password]'
    username = rawInput.split()[1]
    password = rawInput.split()[2]
    check_password = rawInput.split()[3]
    if password != check_password:
        return f'password is not correct'
    return True

def check_login_format(rawInput, login_state):
    if len(rawInput.split()) != 3:
        return f'wrong format for login please input >> login [username] [password]'
    if login_state == True:
        return f'User already login please logout first'
    return True

def check_logout(login_state):
    if login_state == False:
        return f'Please login before logout'
    else:
        print('OK')
    return login_state