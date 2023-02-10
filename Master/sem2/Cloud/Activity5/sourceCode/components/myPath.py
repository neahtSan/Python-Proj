import pathlib
import os

def download_path():
    directory = pathlib.Path(__file__).parent.resolve()
    string_directory = str(directory)
    list_directory = string_directory.split('\\')
    save_directory = '\\'.join(list_directory[0:-1]+['download'])
    
    if not os.path.isdir(save_directory):
        os.mkdir(save_directory)
    
    return save_directory

def upload_path():
    directory = pathlib.Path(__file__).parent.resolve()
    string_directory = str(directory)
    list_directory = string_directory.split('\\')
    save_directory = '\\'.join(list_directory[0:-1]+['upload'])
    
    if not os.path.isdir(save_directory):
        os.mkdir(save_directory)
    
    return save_directory

def all_upload_file():
    # folder path
    dir_path = upload_path()

    # list to store files
    allFile = []

    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            allFile.append(path)
            
    return allFile
    

