import pathlib
import os

#download_path function return download directory in myDropbox_6570108321 directory if no download directory then will create one (take no parameter) 
# Return absolute path to "sourceCode" directory
def download_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
    return os.path.join(parent_dir)

# Return absolute path to "sourceCode" directory
def upload_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
    return os.path.join(parent_dir)

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
    

