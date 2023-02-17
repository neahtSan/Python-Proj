import pathlib
import os

#download_path function return download directory in myDropbox_6570108321 directory if no download directory then will create one (take no parameter) 
def download_path():
    #get path
    directory = pathlib.Path(__file__).parent.resolve()
    string_directory = str(directory)
    list_directory = string_directory.split('\\')
    
    #get download directory
    save_directory = '\\'.join(list_directory[0:-1])
    
    return save_directory

#upload_path function return upload directory in myDropbox_6570108321 directory if no upload directory then will create one (take no parameter) 
def upload_path():
    #get path
    directory = pathlib.Path(__file__).parent.resolve()
    string_directory = str(directory)
    list_directory = string_directory.split('\\')
    
    #get upload directory
    save_directory = '\\'.join(list_directory[0:-1])
    
    return save_directory

#all_upload_file function return all fileName in upload directory 
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
    

