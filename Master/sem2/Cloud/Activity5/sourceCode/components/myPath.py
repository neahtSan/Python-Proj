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

