from components.message import *
from components.logic import *
from components.check import *
from components.user import *

#show greeting message
greet()

notQuit = True
login_state = False
while notQuit:
    try:
        #get input from user
        rawInput = input(">> ")
        command = str()
        
        #check input
        if check_input(rawInput) != True:
            print(check_input(rawInput))
        
        #help manual
        if rawInput == "help":
            help()

        #exit
        if rawInput == "quit":
            notQuit = False
        
        #handle newuser
        if rawInput != '' and rawInput.split()[0] == 'newuser' and len(rawInput.split()) >= 1:
            #newuser
            if check_newuser_format(rawInput) == True:
                command, username, password = user_classified(rawInput, login_state)
            else:
                print(check_newuser_format(rawInput))
        
        #handle login 
        if rawInput != '' and rawInput.split()[0] == 'login' and len(rawInput.split()) >= 1:
            if check_login_format(rawInput, login_state) == True:
                command, username, password = user_classified(rawInput, login_state)
            else:
                print(check_login_format(rawInput, login_state))
            
        #handle logout
        if rawInput != '' and rawInput.split()[0] == 'logout':
            command = user_classified(rawInput, login_state)
        
        #newuser
        if command == 'newuser':
            newuser(username, password)
            
        #login
        if command == 'login':
            login_state = login(username, password, login_state)
        
            
        #logout
        if command == 'logout':
            if check_logout(login_state) == True:
                login_state = False
            else:
                print(check_logout(login_state))
            
        
        if login_state == True:
        #handle put & get command
            if rawInput != '' and rawInput.split()[0] == 'put' and len(rawInput.split()) == 2:
                command, fileName  = rawInput.split()
                
            if rawInput != '' and rawInput.split()[0] == 'get' and len(rawInput.split()) == 3:
                command, fileName, owner  = rawInput.split()
                
            if rawInput != '' and rawInput.split()[0] == 'view':
                command = 'view'

            #view
            if command == "view":
                view(username, password)
                
            #download
            if command == "get":
                get(fileName, username, password, owner)
                
            #upload
            if command == "put":
                put(fileName, username, password)
                
            #share
            if rawInput != '' and rawInput.split()[0] == 'share' and len(rawInput.split()) == 3:
                command, fileName, shared_user = rawInput.split()
                share(fileName, shared_user, username, password)
            
            
    except EOFError as e:
       notQuit = False
        
    





