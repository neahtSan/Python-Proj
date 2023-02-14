from components.message import *
from components.logic import *
from components.check import *

#show greeting message
greet()

notQuit = True
while notQuit:
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
        
    #handle put & get command
    if rawInput != '' and rawInput.split()[0] in ['put', 'get'] and len(rawInput.split()) > 1:
        command, fileName  = rawInput.split()

    #view
    if rawInput == "view":
        view()
        
    #download
    if command == "get":
        get(fileName)
        
    #upload
    if command == "put":
        put(fileName)
        
    





