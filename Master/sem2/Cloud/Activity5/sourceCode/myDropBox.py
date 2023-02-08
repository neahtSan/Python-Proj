from greeting import *
from function import *

greet()

notQuit = True
while notQuit:
    rawInput = input(">> ")

    #exit
    if rawInput == "quit":
        notQuit = False


    if rawInput == "view":
        view()









