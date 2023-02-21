from components.check import *

def user_classified(rawInput, login_state):
    command = '1'; username = '1'; password = '1'
    #newuser
    if rawInput != '' and rawInput.split()[0] in ['newuser']:
        username = rawInput.split()[1]
        password = rawInput.split()[2]
        command = 'newuser'
            
    #login
    if rawInput != '' and rawInput.split()[0] in ['login']:
        username = rawInput.split()[1]
        password = rawInput.split()[2]
        command = 'login'
    
    #logout  
    if rawInput != '' and rawInput.split()[0] in ['logout']:
        command = 'logout'
        return command

    return command, username, password