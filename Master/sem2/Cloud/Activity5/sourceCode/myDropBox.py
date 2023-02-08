from components.message import *
from components.logic import *
from components.check import *

greet()

notQuit = True
while notQuit:
    rawInput = input(">> ")
    
    #check input
    if check_input(rawInput) != True:
        print(check_input(rawInput))

    #exit
    if rawInput == "quit":
        notQuit = False

    #view
    if rawInput == "view":
        view()
        
    









