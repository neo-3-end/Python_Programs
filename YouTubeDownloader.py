# importing the module
from pytube import YouTube

# where to save
SAVE_PATH = "E:/" #to_do

# link of the video to be downloaded
link="https://www.youtube.com/watch?v=yKELA1qBAKA"

try:
	# object creation using YouTube
	# which was imported in the beginning
	yt = YouTube(link)
except:
	print("Connection Error") #to handle exception

# filters out all the files with "mp4" extension
mp4files = yt.streams.filter(progressive=True, file_extension='mp4')
stream = yt.streams.first()

#to set the name of the file


# get the video with the extension and
# resolution passed in the get() function
try:
	# downloading the video
	stream.download(SAVE_PATH)
except:
	print("Some Error!")
print('Task Completed!')
