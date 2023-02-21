
#greet function return string to greeting user when first run the application (take no parameter) 
def greet():
    a = "Welcome to myDropbox Application made by ThaenSan\n"
    b = "==================================================\n"
    c = "Please input command (newuser username password password, login\n"
    d = "username password, put filename, get filename, view, or logout).\n"
    e = "If you want to quit the program just type quit.\n"
    f = "Or input command (help) to see a manual\n"
    g = "=================================================="
    return print(f'{a}{b}{c}{d}{e}{f}{g}')

#help function return string to tell user what command user can use in myDropbox application (take no parameter) 
def help():
    a = "COMMAND\n"
    b = "---------------------------\n"
    c = "view ---> look at files that users have uploaded themselves\n"
    d = "get [file_name] ---> download one file at a time\n"
    e = "put [file_name] ---> upload one file at a time\n"
    f = "quit ---> stop using the myDropbox application\n"
    g = "---------------------------"
    
    return print(f'{a}{b}{c}{d}{e}{f}{g}')