import requests
from io import BytesIO
from PIL import Image

r = requests.get("https://wallpapercave.com/wp/Qsbbfie.png") # requesting an image from the address

print("Status:", r.status_code) # return the status of the request

image = Image.open(BytesIO(r.content)) # Retrieve the data from the request, parsed into bytes, and set to the variable image

path = "./myImage_2." + image.format # create the path the image will be saved to with the name of the file and format

print(image.size, image.format, image.mode) # display image stats

try:
	image.save(path, image.format) # save the image to the path
except IOError:
	print("cannot save image") # display failure text if image save fails
