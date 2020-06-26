from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os


def StartSearch():  # Create a function that can be called in a loop

	search = input("Search for:\t")
	myParams = {"q": search}
	r = requests.get("http://www.bing.com/images/search", params=myParams)

	dirName = search.replace(" ", "_").lower() # create a directory name variable, with spaces replaced by "_", all lowercase

	if not os.path.isdir(dirName): # check of the directory has already been made
		os.makedirs(dirName) # if the directory has not been made, create it

	soup = BeautifulSoup(r.text, "html.parser")
	links = soup.findAll("a", {"class": "thumb"})

	for item in links:
		img_obj = requests.get(item.attrs["href"])
		print("Getting", item.attrs["href"])
		title = item.attrs["href"].split("/")[-1]
		try:
			img = Image.open(BytesIO(img_obj.content))
			img.save("./" + dirName + "/" + title, img.format) # create the file directory for the search query
		except: # create a fail state if save does not work
			print("Could not be saved")

	StartSearch

StartSearch()
