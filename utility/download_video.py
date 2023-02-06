# importing the module
from pytube import YouTube

# where to save
SAVE_PATH = "FOLDER_PATH"

# link of the video to be downloaded
link="VIDEO_LINK"

try:
	# object creation using YouTube
	# which was imported in the beginning
	yt = YouTube(link)
except:
	print("Connection Error") #to handle exception

# filters out all the files with "mp4" extension
mp4files = yt.streams.filter(file_extension='mp4')

stream = yt.streams.get_by_itag(22)
stream.download()
